## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nauraranantya/agentic-generator.git
   cd agentic-generator
   ```
2.	Create and activate a virtual environment:
   ```bash
  python -m venv venv
  source venv/bin/activate       # macOS/Linux
  venv\Scripts\activate          # Windows
  ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Usage

### Option 1: Generate Multi-Agent Code from Knowledge Graph
1. Place the Knowledge Graph (in .ttl or .rdf format) inside the data/ folder, or use the existing dummy data in `data/` or `kg_g3/`.
   Example: `data/dummy_kg.ttl`

2. Run the automated pipeline:
   ```bash
   python runner.py
   ```
   This will automatically:
   - Parse the knowledge graph ontology
   - Generate CrewAI framework code
   - Generate AutoGen framework code

3. Check the `output/` folder for generated scripts:
   - `crewai_generated.py`
   - `autogen_generated.py`

### Option 2: Test Workflow Simulation (Demo)
1. Place your gpt-4o-mini API key in a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

2. Run the pre-configured workflow test:
   ```bash
   python test_email_workflow.py
   ```
   This demonstrates a complete email auto-responder workflow using CrewAI with:
   - Email classification
   - Automated response generation
   - Quality review process

   OR
   
   ```bash
   python test_cust_support_workflow.py
   ```
   This demonstrates a customer support ticket handling workflow using AutoGen with:
   - Ticket classification and prioritization
   - Multi-agent collaboration for resolution
   - Automated response generation
3. View the complete workflow execution and results in the console output.
