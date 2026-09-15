import json
from openai import OpenAI


class ArchitectAgent:

    def __init__(self):
        self.name = "Architect"
        self.client = OpenAI()

    def analyze(self, task):

        prompt = f"""
You are a senior software architect.

Analyze this software requirement:

{task}

Create a software architecture plan with these sections:

1. overview
2. features
3. technology
4. components
5. database
6. api
7. security
8. testing
9. deployment
10. mvp

Return the answer as JSON.
"""

        response = self.client.responses.create(
            model="gpt-5.6",
            input=prompt
        )

        return json.loads(response.output_text)


if __name__ == "__main__":

    agent = ArchitectAgent()

    task = """
  Build a platform for managing a team of AI agents.

The platform should allow users to:
- create and configure AI agents
- organize agents into teams
- assign tasks to agents
- monitor agent execution and statuspython 
- manage agent roles and responsibilities
- review agent outputs
- track tasks, failures, and execution history.
"""

    result = agent.analyze(task)

    print(json.dumps(result, indent=2))