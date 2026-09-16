class DeveloperAgent:

    def __init__(self):
        self.name = "Developer"

    def analyze_architecture(self, architecture):

        print("Developer received architecture.")
        print()
        print("Backend:", architecture.technology.backend)
        print("Database:", architecture.technology.database)
        print("Frontend:", architecture.technology.frontend)