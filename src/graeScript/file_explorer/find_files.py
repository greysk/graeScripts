import os
from pathlib import Path

from graeScript import outfile_path


def search_for(dir: Path | str, glob: str) -> list[Path]:
    """
    Search a directory tree and returns files matching glob.

    Args:
        dir (Path|str): String path to directory to search
        glob (str): Glob pattern for file(s) to find.

    Returns:
        List[Path]: List containing Path objects for files found.
    """
    matching_files = []
    print(f'Searching {dir}...')
    for root, dirs, files in os.walk(dir):
        match_num_in_root = 0
        parent_dir = Path(root)
        for match_file in parent_dir.glob(glob):
            match_num_in_root += 1
            matching_files.append(match_file)
    return matching_files


def found_files_to_txt(dir: Path | str, glob: str, txt_file: Path | str
                       ) -> None:
    """
    Call search_for() and output found file paths to txt_filename.

    Args:
        dir (Path|str): String path to directory to search
        glob (str): Glob pattern for file(s) to find.
        txt_filename (Path|str): File name for txt file.
    """
    found_files = search_for(dir, glob)
    outfile = outfile_path() / f'found_files_{txt_file}'
    print(f'Writing found files to {outfile}')
    with open(outfile, 'w') as f:
        for file in found_files:
            file_p = Path(file)
            di = len(Path(dir).parts)
            directory_rel_filepath = Path('/'.join(file_p.parts[di:]))
            f.writelines(str(directory_rel_filepath) + '\n')
