"""
Auto-generated AutoGen Team: AICrewforscreenwriting
Goals:
  - : Decide whether a text is spam or contains vulgar language and should be filtered (STOP signal).
  - : Analyze discussion, create dialogue-heavy screenplay and format according to requested template.
Capabilities:
  - Spam detection / vulgar content detection: 
  - Discussion analysis and summarization: 
  - Create dialogue-heavy screenplay from discussion: 
  - Text formatting, removing actions/parentheticals: 
  - Score a dialogue on a 1-10 scale: 
Resources:
  - : From: keith@cco.caltech.edu (Keith Allan Schneider)
Subject: Re: <Political Atheists?
Organization: California Institute of Technology, Pasadena
Lines: 50
NNTP-Posting-Host: punisher.caltech.edu

bobbe@vice.ICO.TEK.COM (Robert Beauchaine) writes:

>>I think that about 70% (or so) people approve of the
>>death penalty, even realizing all of its shortcomings.  Doesn't this make
>>it reasonable?  Or are *you* the sole judge of reasonability?
>Aside from revenge, what merits do you find in capital punishment?

Are we talking about me, or the majority of the people that support it?
Anyway, I think that "revenge" or "fairness" is why most people are in
favor of the punishment.  If a murderer is going to be punished, people
that think that he should "get what he deserves."  Most people wouldn't
think it would be fair for the murderer to live, while his victim died.

>Revenge?  Petty and pathetic.

Perhaps you think that it is petty and pathetic, but your views are in the
minority.

>We have a local televised hot topic talk show that very recently
>did a segment on capital punishment.  Each and every advocate of
>the use of this portion of our system of "jurisprudence" cited the
>main reason for supporting it:  "That bastard deserved it".  True
>human compassion, forgiveness, and sympathy.

Where are we required to have compassion, forgiveness, and sympathy?  If
someone wrongs me, I will take great lengths to make sure that his advantage
is removed, or a similar situation is forced upon him.  If someone kills
another, then we can apply the golden rule and kill this person in turn.
Is not our entire moral system based on such a concept?

Or, are you stating that human life is sacred, somehow, and that it should
never be violated?  This would sound like some sort of religious view.
 
>>I mean, how reasonable is imprisonment, really, when you think about it?
>>Sure, the person could be released if found innocent, but you still
>>can't undo the imiprisonment that was served.  Perhaps we shouldn't
>>imprision people if we could watch them closely instead.  The cost would
>>probably be similar, especially if we just implanted some sort of
>>electronic device.
>Would you rather be alive in prison or dead in the chair?  

Once a criminal has committed a murder, his desires are irrelevant.

And, you still have not answered my question.  If you are concerned about
the death penalty due to the possibility of the execution of an innocent,
then why isn't this same concern shared with imprisonment.  Shouldn't we,
by your logic, administer as minimum as punishment as possible, to avoid
violating the liberty or happiness of an innocent person?

keith
  - : Output of spamfilter: either the token STOP (string) or empty/no response.
  - : Detailed analysis identifying speakers, arguments, and distilled points, produced by analyst agent.
  - : Unformatted dialogue-heavy screenplay draft produced by scriptwriter agent (dialogue only, no parentheticals).
  - : Final formatted script output suitable for scoring and display. This resource is the input to the scoring task.
  - : Numeric score assigned by scorer agent (1-10), optionally accompanied by an explanatory text.
"""

from autogen_agentchat.agents import AssistantAgent

from autogen_agentchat.teams import RoundRobinGroupChat

from autogen_agentchat.conditions import (

    MaxMessageTermination

)

from autogen_core.tools import FunctionTool

from autogen_ext.models.openai import (
    OpenAIChatCompletionClient
)

model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini"
)


# ==================================================
# Generated Tool Stubs
# ==================================================


# ==================================================
# Agents
# ==================================================


spamfilter = AssistantAgent(
    name="spamfilter",
    model_client=model_client,
    system_message="""
Role:
spamfilter

Goal:
Decide whether a text is spam or contains vulgar language and should be filtered (STOP signal).

Background:
role: spamfilter; goal: Decide whether a text is spam or not.; backstory: You are an expert spam filter with years of experience. You DETEST advertisements, newsletters and vulgar language.
""",
)


analyst = AssistantAgent(
    name="analyst",
    model_client=model_client,
    system_message="""
Role:
analyse

Goal:
Analyze discussion, create dialogue-heavy screenplay and format according to requested template.

Background:
role: analyse; goal: Distill arguments and identify who said what; backstory: Expert discussion analyst.
""",
)


scriptwriter = AssistantAgent(
    name="scriptwriter",
    model_client=model_client,
    system_message="""
Role:
scriptwriter

Goal:
Analyze discussion, create dialogue-heavy screenplay and format according to requested template.

Background:
role: scriptwriter; goal: Produce dialogue-only screenplay; backstory: hates directional notes
""",
)


formatter = AssistantAgent(
    name="formatter",
    model_client=model_client,
    system_message="""
Role:
formatter

Goal:
Analyze discussion, create dialogue-heavy screenplay and format according to requested template.

Background:
role: formatter; goal: Format text and remove bracketed actions; backstory: expert text formatter.
""",
)


scorer = AssistantAgent(
    name="scorer",
    model_client=model_client,
    system_message="""
Role:
scorer

Goal:
Analyze discussion, create dialogue-heavy screenplay and format according to requested template.

Background:
role: scorer; goal: Score dialogue 1-10; backstory: scoring expert
""",
)



