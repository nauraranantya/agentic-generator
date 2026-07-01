import re

def normalize_ttl(content: str) -> str:
    """Normalize and repair common syntactic/formatting issues in Turtle (.ttl) content."""
    # Repair specific syntax typos from original files
    content = content.replace('description">', 'description>')
    content = content.replace('(see producedResource)." ;', '(see producedResource).""" ;')
    # Repair missing colons on subjects (like chefAgent :agentResourceUsage -> :chefAgent :agentResourceUsage)
    content = re.sub(r'^\s*(?!\ba\b)([a-zA-Z_][a-zA-Z0-9_-]*)\s+(\:\w+)', r':\1 \2', content, flags=re.MULTILINE)

    # 1. Clean markdown code fences (often hallucinated by LLMs)
    content = _strip_markdown_fences(content)
    
    # 2. Fix comment headers and separator characters
    content = _comment_non_rdf_headers(content)
    
    # 3. Comment out YAML/Markdown line separators anywhere in the file
    content = _comment_separators(content)
    
    # 4. Fix syntax errors where properties are incorrectly chained in object position
    content = _fix_invalid_property_objects(content)
    
    # 5. Add missing statement periods ('.') before new subjects
    content = _fix_missing_statement_periods(content)
    
    # 6. Add missing standard prefix declarations
    content = _inject_missing_prefixes(content)
    
    # 7. Repair single-quoted strings that contain physical newlines into triple-quoted strings
    content = _fix_multiline_literals(content)
    
    return content


def _strip_markdown_fences(content: str) -> str:
    """Remove markdown code blocks, e.g., ```turtle or ```."""
    lines = content.splitlines()
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def _comment_non_rdf_headers(content: str) -> str:
    """Comment out non-RDF/Turtle lines at the beginning of the file before any declarations/triples start."""
    lines = content.splitlines()
    cleaned_lines = []
    
    rdf_started = False
    for line in lines:
        stripped = line.strip()
        
        if rdf_started:
            cleaned_lines.append(line)
            continue
            
        # Check if the RDF content starts here
        if stripped.startswith("@prefix") or stripped.startswith("@base") or (stripped and not stripped.startswith("#") and stripped[0] == ":"):
            rdf_started = True
            cleaned_lines.append(line)
            continue
            
        # If RDF hasn't started yet and the line is not empty and not already a comment, we comment it out
        if stripped and not stripped.startswith("#"):
            if stripped == "---":
                cleaned_lines.append("# ---")
            else:
                cleaned_lines.append(f"# {line}")
        else:
            cleaned_lines.append(line)
            
    return "\n".join(cleaned_lines)


def _comment_separators(content: str) -> str:
    """Comment out YAML/Markdown separator lines (like --- or ===) anywhere in the file."""
    content = re.sub(r'^---+$', r'# \g<0>', content, flags=re.MULTILINE)
    content = re.sub(r'^===+$', r'# \g<0>', content, flags=re.MULTILINE)
    return content


def _fix_invalid_property_objects(content: str) -> str:
    """Fix syntax errors where 'dcterms:description' is incorrectly placed in the object position preceding a literal.
    Example: :promptInputData dcterms:description "literal" -> :promptInputData "literal"
    """
    pattern = r'^([ \t]+:\w+)\s+dcterms:description\s+("""[\s\S]*?"""|"[^"\\]*(?:\\.[^"\\]*)*"|\'[^\'\\]*(?:\\.[^\'\\]*)*\')'
    return re.sub(pattern, r'\1 \2', content, flags=re.MULTILINE)


def _replace_last_char(line: str, target: str, replacement: str) -> str:
    # Find the target char before any comment
    parts = line.split('#', 1)
    code_part = parts[0]
    comment_part = f"#{parts[1]}" if len(parts) > 1 else ""
    
    # Strip trailing whitespace from code part and check ending
    stripped_code = code_part.rstrip()
    if stripped_code.endswith(target):
        new_code = stripped_code[:-len(target)] + replacement
        return new_code + code_part[len(stripped_code):] + comment_part
    return line


def _fix_missing_statement_periods(content: str) -> str:
    """Find any statements that are missing a closing period ('.') before a new subject begins, taking care not to modify lines inside multiline string literals."""
    lines = content.splitlines()
    cleaned_lines = []
    
    last_rdf_line_idx = -1
    new_subject_pattern = re.compile(r'^(\:\w+|<\S+>|@prefix|@base)\b')
    
    in_string = False
    string_char = None
    
    for idx, line in enumerate(lines):
        stripped = line.strip()
        
        starts_new_subject = False
        if not in_string and new_subject_pattern.match(line):
            starts_new_subject = True
            
        # Update in_string state by scanning the line
        chars = list(line)
        length = len(chars)
        c_idx = 0
        while c_idx < length:
            if not in_string:
                if c_idx + 2 < length and chars[c_idx] == '"' and chars[c_idx+1] == '"' and chars[c_idx+2] == '"':
                    in_string = True
                    string_char = '"'
                    c_idx += 3
                elif c_idx + 2 < length and chars[c_idx] == "'" and chars[c_idx+1] == "'" and chars[c_idx+2] == "'":
                    in_string = True
                    string_char = "'"
                    c_idx += 3
                elif chars[c_idx] in ('"', "'"):
                    c_idx += 1
                else:
                    c_idx += 1
            else:
                if chars[c_idx] == '\\':
                    c_idx += 2
                    continue
                if chars[c_idx] == string_char and c_idx + 2 < length and chars[c_idx+1] == string_char and chars[c_idx+2] == string_char:
                    in_string = False
                    c_idx += 3
                else:
                    c_idx += 1
                    
        if not stripped or stripped.startswith("#"):
            cleaned_lines.append(line)
            continue
            
        if starts_new_subject:
            if last_rdf_line_idx != -1:
                prev_line = cleaned_lines[last_rdf_line_idx]
                prev_stripped = prev_line.strip()
                if prev_stripped and not prev_stripped.endswith('.'):
                    if prev_stripped.endswith(';'):
                        cleaned_lines[last_rdf_line_idx] = _replace_last_char(prev_line, ';', '.')
                    elif not prev_stripped.endswith((',', '[', ']', '.')):
                        cleaned_lines[last_rdf_line_idx] = prev_line + " ."
                    
        cleaned_lines.append(line)
        if not in_string:
            last_rdf_line_idx = len(cleaned_lines) - 1
            
    return "\n".join(cleaned_lines)


def _inject_missing_prefixes(content: str) -> str:
    """Detect used but undeclared prefixes (e.g. rdf:, rdfs:, dcterms:, xsd:, beam:) and prepend declarations."""
    prefixes_to_add = {
        "rdf": "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .",
        "rdfs": "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        "dcterms": "@prefix dcterms: <http://purl.org/dc/terms/> .",
        "dc": "@prefix dc: <http://purl.org/dc/elements/1.1/> .",
        "xsd": "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .",
        "beam": "@prefix beam: <http://w3id.org/beam/core#> .",
        "pp": "@prefix pp: <http://purl.org/net/p-plan#> .",
    }
    
    declared_prefixes = set(re.findall(r"@prefix\s+(\w+):", content))
    
    used_prefixes = set()
    for match in re.findall(r"\b(\w+):(?!\/\/)\w+", content):
        if match not in {"http", "https"}:
            used_prefixes.add(match)
            
    prefix_declarations = []
    for prefix, decl in prefixes_to_add.items():
        if prefix in used_prefixes and prefix not in declared_prefixes:
            prefix_declarations.append(decl)
            
    if prefix_declarations:
        content = "\n".join(prefix_declarations) + "\n\n" + content
        
    return content


def _fix_multiline_literals(content: str) -> str:
    """Convert single-quoted string literals that span physical newlines into valid triple-quoted string literals."""
    chars = list(content)
    length = len(chars)
    i = 0
    in_string = False
    in_uri = False
    string_char = None  # " or '
    is_triple = False
    upgraded = False
    string_start_idx = -1
    
    result = []
    
    while i < length:
        if not in_string:
            # Handle URIs
            if chars[i] == '<':
                in_uri = True
            elif chars[i] == '>':
                in_uri = False
                
            # Handle comments
            if chars[i] == '#' and not in_uri:
                while i < length and chars[i] != '\n':
                    result.append(chars[i])
                    i += 1
                continue
                
            # Check for triple quotes
            if not in_uri and i + 2 < length and chars[i] == '"' and chars[i+1] == '"' and chars[i+2] == '"':
                in_string = True
                is_triple = True
                upgraded = False
                string_char = '"'
                string_start_idx = len(result)
                result.extend(['"', '"', '"'])
                i += 3
            elif not in_uri and i + 2 < length and chars[i] == "'" and chars[i+1] == "'" and chars[i+2] == "'":
                in_string = True
                is_triple = True
                upgraded = False
                string_char = "'"
                string_start_idx = len(result)
                result.extend(["'", "'", "'"])
                i += 3
            elif not in_uri and chars[i] in ('"', "'"):
                in_string = True
                is_triple = False
                upgraded = False
                string_char = chars[i]
                string_start_idx = len(result)
                result.append(chars[i])
                i += 1
            else:
                result.append(chars[i])
                i += 1
        else:
            # Inside a string literal
            if chars[i] == '\\':
                result.append(chars[i])
                if i + 1 < length:
                    result.append(chars[i+1])
                    i += 2
                else:
                    i += 1
                continue
            
            if is_triple:
                if not upgraded:
                    # Standard triple quote close
                    if chars[i] == string_char and i + 2 < length and chars[i+1] == string_char and chars[i+2] == string_char:
                        in_string = False
                        result.extend([string_char, string_char, string_char])
                        i += 3
                    else:
                        result.append(chars[i])
                        i += 1
                else:
                    # Upgraded triple quote close (originally single-quoted, so it only has one quote at the end)
                    if chars[i] == string_char:
                        in_string = False
                        result.extend([string_char, string_char, string_char])
                        i += 1
                    else:
                        result.append(chars[i])
                        i += 1
            else:
                # Inside single-quoted string literal
                if chars[i] == string_char:
                    in_string = False
                    result.append(chars[i])
                    i += 1
                elif chars[i] == '\n':
                    # Upgrade to triple quotes
                    result.insert(string_start_idx, string_char * 2)
                    is_triple = True
                    upgraded = True
                    result.append(chars[i])
                    i += 1
                else:
                    result.append(chars[i])
                    i += 1
                    
    return "".join(result)
