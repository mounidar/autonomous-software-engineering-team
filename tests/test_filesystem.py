from tools.filesystem import list_files


def test_list_files_excludes_internal_directories(tmp_path):
    # Create a normal source file.
    (tmp_path / "main.py").write_text("print('hello')")

    # Create directories that should be excluded.
    git_dir = tmp_path / ".git"
    git_dir.mkdir()
    (git_dir / "config").write_text("git configuration")

    cache_dir = tmp_path / "__pycache__"
    cache_dir.mkdir()
    (cache_dir / "main.pyc").write_text("cache")

    # Run our filesystem tool.
    files = list_files(tmp_path)

    # Check the result.
    assert str(tmp_path / "main.py") in files
    assert str(git_dir / "config") not in files
    assert str(cache_dir / "main.pyc") not in files