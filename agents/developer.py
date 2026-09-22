from tools.filesystem import list_files


class DeveloperAgent:
    def __init__(self):
        self.name = "Developer"

    def analyze_architecture(self, architecture):
        print("Developer received architecture.")
        print()

        print("Backend:", architecture.technology.backend)
        print("Database:", architecture.technology.database)
        print("Frontend:", architecture.technology.frontend)

    def inspect_repository(self, path="."):
        files = list_files(path)

        print("\nRepository files:")

        for file in files:
            print(file)

        return files