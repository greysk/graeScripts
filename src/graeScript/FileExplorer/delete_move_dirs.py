import logging
import logging.config
import os
from pathlib import Path
import re
from typing import Union

from graeScript.FileExplorer import _WindowsRules, _LinuxRules

logger = logging.getLogger('fileExplorer')


def _validate_args(user_input_args: tuple[str, ...],
                   num_allowed: int,
                   *args: str) -> list:
    """
    Ensures kwargs entered in a function call are acceptable.

    Args:
        input (dict): The kwarg(s) input into a function.
        num_allowed (int): Limit, if any, on number of kwargs allowed.
        args (iterable): The acceptable keys for kwargs.

    Raises:
        SystemExit: Raised if input doesn't match any accepted kwargs.

    Returns:
        list: Containing user_input_args that passed test, if any.
    """
    # Establish lists for testing input and containing inputs that passed.
    acceptable_args = [arg for arg in args]
    lowercase_args = [item.lower() for item in acceptable_args]
    accepted_args = []
    # If user didn't input an arg, skip testing.
    if not len(user_input_args) > 0:
        return []
    # Test user_input_args against acceptable_args.
    for item in user_input_args:
        # Check if non-string args are in acceptable_args.
        if not isinstance(item, str) and item in acceptable_args:
            accepted_args.append(item)
        # Test string args as case-insensitive.
        elif item.lower() in lowercase_args:
            # Ensure output arg is properly cased even if input arg wasn't.
            right_arg = acceptable_args[lowercase_args.index(item.lower())]
            accepted_args.append(right_arg)
        # Skip unacceptable user_input_arg, removing it from args list.
        else:
            print(f'{item} removed - not in {acceptable_args}.')
            continue
    # Return user_input_args that passed test if not more than num_allowed.
    if len(accepted_args) > 0 and len(accepted_args) <= num_allowed:
        return accepted_args
    # Exit program.  user_input_args failed to validate.
    else:
        print('Keyword arg must be no more than'
              f' {num_allowed} of {".".join(acceptable_args)}.')
        raise SystemExit


def _validate_dir(dir: Path) -> Path:
    """
    Ensures dir exists, is a directory, and is an absolute path.

    Args:
        dir (str): String path to directory

    Raises:
        SystemExit: If dir doesn't pass tests, program terminates.

    Returns:
        Path: dir as a pathlib.Path object.
    """
    try:
        dir = Path(dir)
    except PermissionError as e:
        print(e)
        raise SystemExit
    except OSError as e:
        print(e)
        raise SystemExit
    if not dir.is_dir():
        print(f'{dir} must exist and be a directory.')
        raise SystemExit
    if not dir.is_absolute():
        print(f'{dir} must be an absolute path.')
        raise SystemExit
    return dir


def _validate_dirs(*args: Path) -> list[Path]:
    """
    Ensures dirs exist, are directories, and are absolute paths.

    Returns:
        list[Path]: contains validated dirs.
    """
    validated_dirs = []
    for dir in args:
        try:
            validated_dirs.append(_validate_dir(dir))
        except SystemExit:
            continue  # Check next dir even if one failed.
    if not validated_dirs:
        raise SystemExit
    return validated_dirs


def _validate_path(path: Path) -> Path:
    """
    Ensures dir exists, is a directory, and is an absolute path.

    Args:
        dir (str): String path to directory

    Raises:
        SystemExit: If dir doesn't pass tests, program terminates.

    Returns:
        Path: dir as a pathlib.Path object.
    """
    try:
        path = Path(path)
    except PermissionError as e:
        print(e)
        raise SystemExit
    except OSError as e:
        print(e)
        raise SystemExit
    if not path.is_file() and not path.is_dir():
        print(f'{path} must exist and be a directory.')
        raise SystemExit
    if not path.is_absolute():
        print(f'{path} must be an absolute path.')
        raise SystemExit
    return path


def _validate_paths(*args: Path) -> list[Path]:
    """
    Ensures dirs exist, are directories, and are absolute paths.

    Returns:
        list[Path]: contains validated dirs.
    """
    validated_paths = []
    for dir in args:
        try:
            validated_paths.append(_validate_paths(dir))
        except SystemExit:
            continue  # Check next dir even if one failed.
    if not validated_paths:
        raise SystemExit
    return validated_paths


def _block_protected(*args: Path, rule_group: str = 'all') -> list[Path]:
    # [ ] Write tests for
    """
    Blocks setting a input directory to certain directories.

    Which are blocked is based on variables within code.

    Args:
        input_directory (str): an input directory.

    Raises:
        SystemExit: If input directory matches blocked directories

    Returns:
        list[Path]: List of any PathObj dirs that passed tests.
    """
    passed_dirs = []
    for path in args:
        path = _validate_path(path)
        if path.drive:
            is_not_blocked = _WindowsRules().check_against(path, rule_group)
        else:
            is_not_blocked = _LinuxRules().check_against(path, rule_group)
        if is_not_blocked:
            passed_dirs.append(is_not_blocked)
    if not passed_dirs:
        raise SystemExit
    return passed_dirs


def _join_subpath(root: Path, source: Union[str, Path],
                  destination: Path) -> Path:
    """
    Appends to destination, source-relative path to root.

    Written for use with os.walk() to match subfolders during walk.

    For example:
       root = 'R:/Documents/School/Math
       source = 'R:/Documents/School'
       destination = 'J:/Classwork'

       Returns: pathlib.Path('J:/Classwork/Math')

    Args:
        root (str|Path): Path object for root/current dir in os.walk().
        source (str|Path): Path object to dir above root dir.
        destination (str|Path): Path object to different dir above root dir.

    Returns:
        Path: Path object of destination subfolders matching root
              subfolders relative to source.
    """
    root = _validate_dir(root)
    source = Path(source)
    destination = Path(destination)
    if root == source:
        # No change needed, root is the same path as source.
        return destination
    else:
        # Obtain number of Path parts in source.
        i = len(source.parts)
        # Return destination + parts of root longer than source.
        return destination / '/'.join(root.parts[i:])


def rename_file(source: Path, destination: Path,
                test: bool = True) -> None:
    """
    Renames source file to destination file.

    Args:
        source (str|Path): Absolute path object of file to be renamed.
        destination (str|Path): Path to which to rename source.
        test (bool, optional): If True, no file changes are made.
                               Default is True.
    """
    source = Path(source)
    destination = Path(destination)
    if test:
        print('--Test only--')
    else:
        # Rename/Move file
        source.rename(destination)
    print('Renamed/Moved:')
    print(f'\t- source: {source}\n\t+ destination: {destination}')


def delete_file(file: Path, test: bool = True) -> None:
    """
    Deletes file.

    Args:
        file (str|Path): Absolute path to file to be deleted.
        test (bool, optional): If True, no file changes are made.
                               Defaults to True.
    """
    # [ ]: Create a validate_file/path to ensure file is absolute.
    if test:
        print('Test only')
        file = _block_protected(file)
    else:
        # Only deletes file if test is False.
        file.unlink()
    print('Deleted:')
    print(f'\t- file: {file}')


def delete_folder(dir: str, test: bool = True) -> None:
    """
    Deletes dir if it is empty. Uses block_protected() before deleting.

    Args:
        dir (str|Path): Absolute path to directory to delete.
        test (bool, optional): If True, no file changes are made.
                               Defaults to True.

    Raises:
        OSError: If test is True and files are in dir.
    """
    # Makes sure dir is an existing dir with an absolute path.
    directory = _validate_dir(dir)
    if test:
        print('Test only')
        # Test for delete failure due to files in directory.
        directory = _block_protected(dir)
        files_in = [item for item in dir.iterdir()]
        if files_in:
            print(f'Unable to delete {dir}')
            raise OSError
    else:
        # Ensures folder isn't one that shouldn't be deleted.
        directory = _block_protected(dir)
        directory[0].rmdir()
    print('Deleted:')
    print(f'\t- folder: {dir}')


def delete_empty_tree(directory: Path, test: bool = True) -> None:
    """
    Deletes empty folders within directory's tree.

    Args:
        directory (str|PathObj): Absolute path to top directory.
        test (bool, optional): If True, no file changes are made.
                               Defaults to True.
    """
    # Makes sure directory is an existing dir with an absolute path.
    directory = _validate_dir(directory)
    for root, dirs, files in os.walk(directory, False):
        current_loop_dir = Path(root)
        for dir in dirs:
            # Get absolute path to dir within current_loop_dir.
            dir_path = current_loop_dir / dir
            try:
                # Path testing and deleting handled by function.
                delete_folder(dir_path, test)
            except OSError:
                continue


def glob_delete(dir: Path, glob_pattern: str, test: bool = True) -> None:
    """
    Deletes files in a directory based on glob pattern.

    Args:
        dir (str): Absolute path to directory containing files to be deleted.
        glob_pattern (str): Glob pattern identifying file to delete.
        test (bool, optional): If True, no file changes are made.
                               Default is True.

    Returns:
        NoneType: None
    """
    # Makes sure dir is an existing dir with an absolute path.
    dir = _validate_dir(dir)
    for root, directories, files in os.walk(dir):
        current_loop_dir = Path(root)
        for file in current_loop_dir.glob(glob_pattern):
            try:
                # Path testing and deleting handled by function.
                delete_file(dir, test)
            except FileNotFoundError:
                print(f'{file} not found to delete.')


def move_contents(source: Path, destination: Path, test: bool = True,
                  *args: str) -> list[dict[str, object]]:
    """
    Moves all of source's contents into destination.

    Args:
        source (str): Absolute path to folder from which files will be moved.
        destination (str): The folder into which files will be moved.
        test (bool, optional): If True, no file changes are made.
                               Default is True.
        *args (str, optional):
            replace: Replace any destination files matching source files.
            delete: Delete any source files matching destination files.
            compare: Keep the file with the most recent edit date.

    Returns:
        List[dict]: Contains information for every file left in source.
                    Dict keys: 'root', 'filename', 'destination'. Respectively:
                    the path to parent directory of file, the file's filename,
                    and the path to the duplicate file in destination.
    """
    # Make sure any *args entered are acceptable for function.
    on_file_conflict = _validate_args(args, 1,
                                      'replace', 'delete', 'compare')
    # Make sure source and destination are existing dirs & absolute paths.
    source = _validate_dir(source)
    destination = _validate_dir(destination)
    unmoved_files = []
    for root, dir, source_files in os.walk(source):
        current_loop_dir = Path(root)
        # Make destination path match current source (sub)directory.
        dest = _join_subpath(current_loop_dir, source, destination)
        # Walk through files in current_loop_dir folder.
        for source_file in source_files:
            # Create absolute path to source_file and its move_to destination.
            src_file_path = current_loop_dir / source_file
            move_to = dest
            try:
                move_to_files = [file.name for file in move_to.iterdir()]
            except FileNotFoundError:
                move_to_files = []
            move_to = move_to / src_file_path.name
            # Check for any source files matching destination files.
            if src_file_path.name not in move_to_files:
                # [ ]: Change to use iterdir in move_to parent.
                # Move source_file. File doesn't already exist in destination.
                rename_file(src_file_path, move_to, test)
                continue
            # File exists in destination.
            if on_file_conflict[0] == 'replace':
                # Replace file in destination.
                rename_file(src_file_path, move_to, test)
            elif on_file_conflict[0] == 'delete' and src_file_path.is_file():
                # Delete file in source.
                delete_file(src_file_path, test)
            elif on_file_conflict[0] == 'compare':
                # Keep file with most recent last edit date.
                source_file_edit_date = src_file_path.stat().st_mtime
                dest_file_edit_date = move_to.stat().st_mtime
                if source_file_edit_date > dest_file_edit_date:
                    # Replace move_to file.  source_file was last edited one.
                    rename_file(src_file_path, move_to, test)
                else:
                    # Delete source_file.  move_to file was last edited one.
                    delete_file(src_file_path, test)
            else:  # No arg entered - skip source_file already in move_to.
                print('Skipped:')
                print(f'\t= source: {source_file}\n\t= destination: {move_to}')
                unmoved_files.append({'root': root,
                                      'filename': src_file_path.name,
                                      'destination': move_to})
    # Delete empty folders in source's tree.
    delete_empty_tree(source, test)
    # Return any unmoved files.
    return unmoved_files


def walk_and_combine(start_dir: Path, dest_pattern: str,
                     match_group_num: int, test: bool = True,
                     *args: str) -> None:
    # [ ] Test
    """
    Walk through start_dir tree and combine dirs matching regex dest_pattern.

    Args:
        start_dir (str|PathObj): Absolute path to directory at which to start.
        dest_pattern (str): A string regex pattern to find folders to combine.
                            Files will be moved into folder matching this.
        match_group (int): The Match object group number to use to find
                           folders to move files from.
        test (bool, optional): If True, no file changes are made.
                               Defaults to True.
        *args (str, optional):
            replace: Replace any destination files matching source files.
            delete: Delete any source files matching destination files.
            compare: Keep the file with the most recent edit date.

    For example:

        walk_and_combine(
            start_dir='R:/School',
            dest_pattern=r'^([1-2][0-9][0-9][0-9] - )(.*)',
            match_group=2,
            test=False,
            args='replace')

       ---- BEFORE PROGRAM ----

        R:/School
         |_ JuniorYear
            |_ 1999 - Math
                |_ to_memorize.txt
            |_ Math
                |_ Notes
                    |_ FinalNotes.txt
         |_ SeniorYear
            |_ 2000 - Lab Work
                |_ Homework
                    |_ Lesson2.txt
            |_ Lab Work
                |_ Homework
                    |_ Lesson2.txt
                |_ Experiments.txt

       ---- AFTER PROGRAM RUNS ----

        R:/School
         |_ JuniorYear
            |_ 1999 - Math
                |_ Notes
                    |_ FinalNotes.txt
                |_ to_memorize.txt
         |_ SeniorYear
            |_ 2000 - Lab Work
                |_ Homework
                    |_ Lesson2.txt
                |_ Experiments.txt

    """
    pattern = re.compile(rf'{dest_pattern}', re.IGNORECASE)
    # Makes sure start_dir is an existing dir with an absolute path.
    start_dir = _validate_dir(start_dir)

    for root, directories, files in os.walk(start_dir):
        current_loop_dir = Path(root)
        # Try to match folders within current_loop_dir to regex pattern.
        regex_match_results = map(pattern.match, directories)
        for regex_match in regex_match_results:
            if regex_match is None:
                # Skip directories that didn't match regex pattern.
                continue
            # Create absolute path to regex_matched_dir.
            regex_matched_dir = current_loop_dir / regex_match.group(0)
            to_compare = regex_match.group(match_group_num)
            # In current_loop_dir, find directories names equal to to_compare.
            for dir in directories:
                if dir.lower() != to_compare.lower():
                    # Skip directories whose names don't equal to_compare.
                    continue
                duplicate_dir = current_loop_dir / dir
                # Move contents of duplicate_dir to regex_match dir.
                move_contents(duplicate_dir, regex_matched_dir, test, *args)


if __name__ == "__main__":
    pass
