from pathlib import Path

# [ ] Write docstrings


def change_file_ext(file: Path | str, new_ext: str, Test: bool = True) -> None:
    file = Path(file)
    new_file_name = file.with_suffix(new_ext)
    if not Test:
        file.replace(new_file_name)
    print(f'Renamed:  {file.name}\n   to     {new_file_name.name}')


def change_file_ext_in(dir: Path | str, new_ext: str, replace_ext: str = '*.*',
                       Test: bool = True) -> None:
    dir = Path(dir)
    for file in dir.glob(replace_ext):
        change_file_ext(file, new_ext, Test)
