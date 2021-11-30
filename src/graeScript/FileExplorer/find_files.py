import os
from pathlib import Path
from typing import List


def search_for(directory: str, glob: str) -> List[Path]:
    """
    Searches a directory tree and returns files matching glob.

    Args:
        directory (str): String path to directory to search
        glob (str): Glob pattern for file(s) to find.

    Returns:
        List[Path]: List containing Path objects for files found.
    """
    matching_files = []
    print(f'Searching {directory}...')
    for root, dirs, files in os.walk(directory):
        match_num_in_root = 0
        parent_dir = Path(root)
        for match_file in parent_dir.glob(glob):
            match_num_in_root += 1
            matching_files.append(match_file)
    return matching_files


def found_files_to_txt(directory: str, glob: str, txt_filename: str) -> None:
    """
    Calls search_for() and outputs found file paths to txt_filename.txt.

    Args:
        directory (str): String path to directory to search
        glob (str): Glob pattern for file(s) to find.
        txt_filename (str): File name for txt file.
    """
    found_files = search_for(directory, glob)
    print(f'Writing found files to {txt_filename}')
    with open(('found_files_' + txt_filename), 'w') as f:
        for file in found_files:
            file_p = Path(file)
            di = len(Path(directory).parts)
            directory_rel_filepath = Path('/'.join(file_p.parts[di:]))
            f.writelines(str(directory_rel_filepath) + '\n')


if __name__ == '__main__':
    pass
