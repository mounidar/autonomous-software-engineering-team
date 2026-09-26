from tools.filesystem import list_files, read_file, write_file


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

    def read_repository_file(self, path):
        content = read_file(path)

        print(f"\nContents of {path}:")
        print(content)

        return content

    def write_repository_file(self, path, content):
        written_path = write_file(path, content)

        print(f"\nDeveloper wrote file: {path}")

        return written_path