from pathlib import Path


def change_file_ext(filename: str, new_ext: str, runTest: bool = True) -> None:
    file = Path(filename)
    new_file_name = file.with_suffix(new_ext)
    if not runTest:
        file.replace(new_file_name)
    print(f'Renamed:  {file.name}\n   to     {new_file_name.name}')


def change_file_ext_in(folder: str, new_ext: str, replace_ext: str = '*.*',
                       runTest: bool = True) -> None:
    dir = Path(folder)
    for file in dir.glob(replace_ext):
        change_file_ext(file, new_ext, runTest)
