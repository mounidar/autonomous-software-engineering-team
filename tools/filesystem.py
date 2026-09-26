from pathlib import Path


def list_files(path="."):
    root = Path(path)

    excluded_directories = {
        ".git",
        "__pycache__",
        ".pytest_cache",
        ".venv",
        "venv",
    }

    return [
        str(file)
        for file in root.rglob("*")
        if file.is_file()
        and not any(part in excluded_directories for part in file.parts)
    ]


def read_file(path, root="."):
    root_path = Path(root).resolve()
    file_path = (root_path / path).resolve()

    if not file_path.is_relative_to(root_path):
        raise ValueError("Cannot read files outside the project directory.")

    return file_path.read_text(encoding="utf-8")



def write_file(path, content, root="."):
    root_path = Path(root).resolve()
    file_path = (root_path / path).resolve()

    if not file_path.is_relative_to(root_path):
        raise ValueError("Cannot write files outside the project directory.")

    file_path.parent.mkdir(parents=True, exist_ok=True)

    file_path.write_text(content, encoding="utf-8")

    return str(file_path)


if __name__ == "__main__":
    files = list_files(".")

    for file in files:
        print(file)
