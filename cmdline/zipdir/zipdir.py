#! python3
# zipfolder.py
'''Copies and entire folder and its contents into a ZIP file.

The zip file's file name automatically increments.'''
from pathlib import Path
import re
import sys
import zipfile


def pathwalk(dir: Path) -> list[Path]:
    """Obtain all file paths in a directory and all it's subdirectories.

    Function is recursive.

    Args:
        `dir` (`Path`): The starting, top-level directory to walk.

    Returns:
        (list): Containing Path objects of all filepaths in `dir`.
    """
    # Obtain all folders within dir.
    subdir_folders = [item for item in dir.iterdir() if item.is_dir()]
    # Obtain all files within dir.
    subfiles = [item for item in dir.iterdir() if item.is_file()]

    # Use recursion to get paths to all files within dir.
    if subdir_folders:
        # Obtain file paths from the subdirectories within dir and
        # add them to the subfiles list.
        for folder in subdir_folders:
            subfiles.extend(pathwalk(folder))
    # When dir contains no folder, return the subfiles list.
    return subfiles


def folder2zip(dir: str | Path) -> None:
    """
    Back the contents of `dir` in a zip file in `dir`'s parent directory.

    If a zip file already exist with the same name, the number in the zip file
    name is automatically incremented. Otherwise, the zip file name will be
    `{dir}(1).zip`

    Args:
        `dir` (str | Path): The absolute path to the folder to be compressed.
    """
    # Make the path to the folder an absolute path, if it isn't already.
    dir: Path = dir.absolute()
    dirzipped_regex = re.compile(fr'{dir.stem}\(([\d]+)\).zip')
    # Create the filename for the zip file to avoid overwriting existing
    # files, if any.
    number = 1
    while True:
        zipfilename = dir.with_name(f'{dir.stem}({str(number)}).zip')
        if not zipfilename.exists():
            # Stop increasing number.
            break
        number += 1
    # Create empty zip file to start compression.
    print(f'Creating {zipfilename}...')
    new_zipfile = zipfile.ZipFile(zipfilename, 'w',
                                  compression=zipfile.ZIP_LZMA)
    # Add all files in `dir`'s file tree to the zip file.
    files_in_dir = pathwalk(dir)
    for file in files_in_dir:
        match = dirzipped_regex.match(file.name)
        if match:
            # Don't add zip of dir to zipfile
            continue
        # Create path relative to dir's parent for archive because every folder
        # that is in the filepath will be created in the zipfile.
        archivename = file.relative_to(dir.parent)
        new_zipfile.write(file, archivename)
    new_zipfile.close()
    print('Done')


if __name__ == "__main__":
    # If command line arguments, use path given. Otherwise, use cwd.
    if len(sys.argv) > 1:
        folder_path = sys.argv[1:]
        # If path argument is multiple parts, assume spaces between and join.
        if len(folder_path) > 1:
            folder_path = ' '.join(folder_path)
        # Otherwise, take just first item in list
        else:
            folder_path = folder_path[0]
    # If no path entered in command line, use the current working directory.
    else:
        folder_path = ('')

    folder2zip(Path(folder_path))
