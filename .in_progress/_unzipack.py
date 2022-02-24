#! python3
"""Unzip AutoBor files into User/Documents and moves .py files to subdirectory.
Written second compared to unzipack.py
"""
from pathlib import Path
import re
import sys
import shutil
import zipfile as zf


def test_zip(file):
    """
    Tests that file exists and doesn't contain bad files.

    Args:
        file (string|Path): Path/string path to a zipfile to test.
    """
    zipfile = Path(file)
    try:
        f = zf.ZipFile(zipfile)
    except FileNotFoundError:
        print(f'No such file or directory: {zipfile}')
        sys.exit()
    else:
        bad_file = f.testzip()
        f.close()
        if bad_file:
            print(f'Bad file ({bad_file})found in {zipfile.name}.')
            print('Canceling unzipping of file.')
            sys.exit()


def unzip(to_unzip, destination, overwrite=False, move_files=False):
    """
    Unzips files to unzip_to.

    Args:
        to_unzip (Path|str):
            Location of the zipfile to be unzipped.
        unzip_to (Path|Str):
            Directory where to unzip zipfile into.
        overwrite (bool, optional):
            If True, existing filenames in conflict are overwritten.
            Defaults to False.
        move_files (bool, optional):
            If True, Moves files from unzipped directory into unzip_to.
            Defaults to True.
    """
    zipfile = Path(to_unzip)
    test_zip(zipfile)
    unzip_to = Path(destination)
    # Obtain files and directories contained in the zipfile.
    zippedfiles = set([item.filename for item in zf.ZipFile(zipfile).infolist()
                      if not item.is_dir()])
    zipfile1 = list(zf.ZipFile(zipfile).infolist())
    # Assume first dir in zipfile is the parent directory of entire zipfile.
    if zipfile1[0].is_dir():
        unzipped_dir = unzip_to / (zipfile1[0].filename.replace('/', ''))
    else:
        unzipped_dir = unzip_to / zipfile.stem
        unzip_to = unzipped_dir
    # Get set of files if unzipped_dir already exists.
    try:
        # TODO: Fix to account for subfolders
        unzippedfiles = set([file.name for file in unzipped_dir.iterdir()])
    except FileNotFoundError:
        pass

    if not unzipped_dir.is_dir() or overwrite:
        # Either unzipped_dir doesn't exist or overwrite is True.
        # Extract zipfile into destination.
        print(f'Extracting {zipfile.name} into {unzip_to}...')
        with zf.ZipFile(zipfile) as f:
            f.extractall(unzip_to)
        # To test success
        unzip(zipfile, destination, overwrite=False)
    # TODO: Fix to account for subfolders. In the zippedfiles: subfolder/file.
    # elif zippedfiles.difference(unzippedfiles):
    #     # zipfile contains some files not in unzipped_dir.
    #     # Extract only files in zipfile not already in unzipped_dir.
    #     not_shared = zippedfiles.difference(unzippedfiles)
    #     for item in not_shared:
    #         print(f'Unzipping only files in {zipfile.name} that are not'
    #               f'already in {unzip_to}...')
    #         with zf.ZipFile(zipfile) as f:
    #             f.extract(item)
    #     # To either move up files or terminate program.
    #     unzip(zipfile, destination, overwrite=False)
    elif zippedfiles.issubset(unzippedfiles):
        # All files in zipfile exist in destination.
        if move_files:
            # Call move_contents_up() to move files in unzipped_dir.
            print(f'{zipfile.name} and all contents exists in {unzip_to}.')
            print('Moving on to unpack the unzipped directory.')
            move_contents_up(unzipped_dir)
        else:
            # Program complete. All files unzipped.
            print(f'{zipfile.name} and all contents exists in {unzip_to}.')
            print('Done!')
            sys.exit()
    else:
        # directory exists in destination with same name as unzipped_dir, but
        # contains no files in common. Exits for safety.
        print(f'{unzipped_dir} exists in {destination}',
              f'and contains no files in common with {zipfile}.')
        print('Exiting...')
        sys.exit()


def move_contents_up(dir_to_unpack):
    to_unpack = Path(dir_to_unpack)
    files_to_unpack = set(to_unpack.iterdir())
    parent = to_unpack.parent
    files_in_parent = set(to_unpack.parent)
    total_files = len(files_to_unpack)

    print(f'Moving files from `{to_unpack}`` to `{parent}`.')
    if overwrite:
        # Move all files up one level
        for file in files_to_unpack:
            print(f'Moving {file.name} to {parent+file.name}...')
            # shutil.move(file, parent+file.name)
    else:
        # Move only files not already in parent directory.
        for file in files_to_unpack.difference(files_in_parent):
            print(f'Moving {file} to {parent+file.name}...')
            # shutil.move(file, parent+file.name)
        unmoved = list(to_unpack.iterdir())
        if unmoved:
            print(f'{len(unmoved)}/{total_files} already existed in {parent}.'
                  f'Files not moved from {to_unpack}.')
            print('Exiting.')
            sys.exit()
    print('All files moved to parent directory.')
    # Try to delete empty to_unpack directory.
    try:
        to_unpack.rmdir()
    except:
        pass
    else:
        print(f'Deleted empty {to_unpack}')
    # If user has files to sort, call storefiles(). Otherwise, done!
    if file_ext_to_sort:
        storefiles(directory=parent, file_globs=file_ext_to_sort)
    else:
        print('Done!')
        sys.exit()


def storefiles(directory, file_globs):
    """
    Move directories in a directory to a subdirectory based on glob patterns.

    Args:
        directory (path-like): a string path/Path to directory to sort.
        file_globs (list): a list of strings of glob patterns.
    """
    to_sort = Path(directory)
    print(f'Sorting files in {to_sort}...')
    for pattern in file_globs:
        # Create folder for files sorted per this glob pattern.
        rp = re.compile(r'([0-9a-zA-Z_])+')
        sorted_dir = to_sort / (rp.match(pattern).group(0) + '_files')
        # sorted_dir.mkdir()
        print(sorted_dir)
        # Move files from directory to subfolder sorted_dir.
        for file in to_sort.glob(pattern):
            print(f'Moving {file.name} to {sorted_dir+file.name}.')
            # shutil.move(file, sorted_dir+file.name)
    print('Done!')


def main():
    """Called below to start program when run as a script."""
    unzip(to_unzip, unzip_to, overwrite, move_files)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage:')
        print('unzipack.py to_unzip [unzip_to=to_unzip.parent]',
              '[bool_overwrite=False] [bool_move_up=False]',
              '[file_ext_to_sort=.py*]')
        raise SystemExit
    # At least required arguments provided:
    to_unzip = Path(sys.argv[1])

    # Set defaults/optional arguments:
    unzip_to = to_unzip.parent
    overwrite = False
    move_files = False
    file_ext_to_sort = ''

    # To Set Optional Arguments Provided.
    if len(sys.argv) >= 3:
        unzip_to = Path(sys.argv[2])
    if len(sys.argv) >= 4:
        overwrite = sys.argv[3]
    if len(sys.argv) >= 5:
        move_files = sys.argv[4]
        if move_files and len(sys.argv) >= 6:
            file_ext_to_sort = sys.argv[5:]

    # Call main()
    main()
