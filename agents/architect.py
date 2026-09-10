from openai import OpenAI

client = OpenAI()


class ArchitectAgent:

    def __init__(self):
        self.name = "Architect"

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

        response = client.responses.create(
            model="gpt-5.6",
            input=prompt
        )

        return response.output_text


if __name__ == "__main__":

    agent = ArchitectAgent()

    task = "Build a task management web application."

    result = agent.analyze(task)

    print(result)