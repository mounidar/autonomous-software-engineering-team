from pathlib import Path


def list_files(path="."):
    root = Path(path)

    excluded_directories = {".git", "__pycache__", ".venv", "venv"}

    return [
        str(file)
        for file in root.rglob("*")
        if file.is_file()
        and not any(part in excluded_directories for part in file.parts)
    ]


if __name__ == "__main__":
    files = list_files(".")

    for file in files:
        print(file)