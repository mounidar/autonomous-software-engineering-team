class DeveloperAgent:

    def __init__(self):
        self.name = "Developer"

    def analyze_architecture(self, architecture):

        technology = architecture["technology"]

        print("Developer received architecture.")
        print()
        print("Backend:", technology["backend"]["framework"])
        print("Database:", technology["data"]["transactional_database"])
        print("Database Access:", technology["backend"]["database_access"])


if __name__ == "__main__":

    developer = DeveloperAgent()

    architecture = {
        "technology": {
            "backend": {
                "framework": "FastAPI",
                "database_access": "SQLAlchemy + Alembic"
            },
            "data": {
                "transactional_database": "PostgreSQL"
            }
        }
    }

    developer.analyze_architecture(architecture)
