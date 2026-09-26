from agents.architect import ArchitectAgent
from agents.developer import DeveloperAgent


task = """
Build a platform for managing a team of AI agents.

The platform should allow users to:
- create and configure AI agents
- organize agents into teams
- assign tasks to agents
- monitor agent execution and status
- manage agent roles and responsibilities
- review agent outputs
- track tasks, failures, and execution history
"""


architect = ArchitectAgent()

architecture = architect.analyze(task)
print("\nARCHITECT OUTPUT:")
print(architecture)
print()
developer = DeveloperAgent()

developer.analyze_architecture(architecture)
developer.inspect_repository(".")
developer.read_repository_file("README.md")

