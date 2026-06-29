"""
Auto-generated CrewAI Crew: AICrewforscreenwriting

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
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

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task




@CrewBase
class AICrewforscreenwriting:
    """AICrewforscreenwriting crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def spamfilter(self) -> Agent:
        return Agent(
            config=self.agents_config['spamfilter'],
            allow_delegation=True,
            verbose=True,
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'],
            allow_delegation=True,
            verbose=True,
        )

    @agent
    def scriptwriter(self) -> Agent:
        return Agent(
            config=self.agents_config['scriptwriter'],
            allow_delegation=True,
            verbose=True,
        )

    @agent
    def formatter(self) -> Agent:
        return Agent(
            config=self.agents_config['formatter'],
            allow_delegation=True,
            verbose=True,
        )

    @agent
    def scorer(self) -> Agent:
        return Agent(
            config=self.agents_config['scorer'],
            allow_delegation=True,
            verbose=True,
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def task1_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['task1_analysis'],
            agent=self.analyst(),
        )

    @task
    def task2_scriptwriting(self) -> Task:
        return Task(
            config=self.tasks_config['task2_scriptwriting'],
            agent=self.scriptwriter(),
            context=[self.task1_analysis()],
        )

    @task
    def task3_formatting(self) -> Task:
        return Task(
            config=self.tasks_config['task3_formatting'],
            agent=self.formatter(),
            context=[self.task2_scriptwriting()],
        )

    @task
    def task0_spam_check(self) -> Task:
        return Task(
            config=self.tasks_config['task0_spam_check'],
            agent=self.spamfilter(),
        )

    @task
    def task4_scoring(self) -> Task:
        return Task(
            config=self.tasks_config['task4_scoring'],
            agent=self.scorer(),
            context=[self.task3_formatting()],
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the AICrewforscreenwriting"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
