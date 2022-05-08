#! python3
"""Change the newlines of a file or multiple files to LF."""
import io
import logging
from pathlib import Path

log_file = Path("~/file2lf_test_output.log").expanduser()
logging.basicConfig(filename=log_file,
                    encoding='utf-8', level=logging.INFO)
logging.debug('----- Start new program run -----')


# Only files with extensions matching those in this set will be changed.
PLAINTEXT = {'.srt', '.txt', '.html', '.asc', '.csv', '.plist', '.xlog',
             '.sub', '.rdf', '.lst', '.htm', '.md', '.bas', '.tsv', '.txt',
             '.text', '.pod', '.cfd', '.pl', '.ascii', '.html5', '.yml',
             '.xsd', '.sbv', '.att', '.py', '.pyw', '.css', '.js', '.sql',
             '.json', '.xml', '.c', '.h', '.vtt', 'htmls', '.srt', 'vb', }


def pathwalk(dir: Path, matching_ext: set | None = PLAINTEXT) -> list[Path]:
    """Obtain file paths in a directory and all it's subdirectories.

    Function is recursive.

    Args:
        `dir` (`Path`): The starting, top-level directory to walk.

    Returns:
        (list): Containing Path objects of all filepaths in `dir` matching
        glob_pattern.
    """
    # Obtain all folders within dir.
    subdir_folders = [item for item in dir.iterdir() if item.is_dir()]
    if matching_ext is not None:  # Obtain all files within dir.
        subfiles = [item for item in dir.iterdir()
                    if item.is_file() and item.suffix in matching_ext]
    else:  # Obtain all files within dir.
        subfiles = [item for item in dir.iterdir if item.is_file()]

    # Use recursion to get paths to all files within dir.
    if subdir_folders:
        # Obtain file paths from the subdirectories within dir and
        # add them to the subfiles list.
        for folder in subdir_folders:
            subfiles.extend(pathwalk(folder))
    # When dir contains no folder, return the subfiles list.
    return subfiles


def file2newLF(file: Path, outpath: Path | None = None, *,
               test: bool = True, verbose: bool = False) -> None:
    """
    Output copy of text file to outpath with LF newline endings.

    Args:
        file (Path): The file to be replaced.
        outpath (Path): The path for the output file.
        test (bool, optional): If False, file is replaced.
            If True, file is not replaced. Defaults to True.
        verbose (bool, optional): Prints files being overwritten to terminal.
            Defaults to False.

    Raises:
        SystemExit: If Outpath already exists.
    """
    if outpath.exists():  # Exit program
        print(f'Output file already exists: {outpath}')
        print('Exiting...')
        raise SystemExit
    if verbose:  # Print files being converted to LF
        print(f'Converting newline ending to LF in {str(file)}')
        print(f'Outputting file to {outpath}')
    if not test:  # Output converted files.
        with open(file, mode='r') as i, open(outpath, mode='w') as o:
            o.write(i.read())
    print('Done')


def file2LF(file: Path, *, test: bool = True, verbose: bool = False) -> None:
    """
    Overwrite existing text file with same file, but with LF newline endings.

    Args:
        file (Path): The file to be replaced.
        test (bool, optional): If False, file is replaced.
            If True, file is not replaced. Defaults to True.
        verbose (bool, optional): Prints files being overwritten to terminal.
            Defaults to False.
    """
    # File will be overwritten; read contents into memory and close.
    membuffer = io.StringIO()
    membuffer.write(file.read_text())
    membuffer.seek(0)
    if verbose:  # Print files being changed to console.
        print(f'Replacing newline ending to LF in {str(file)}')
    if not test:  # Replace file.
        with open(file, mode='w', newline='\n') as f:
            # Write contents from previous version of file into the new file.
            f.write(membuffer.getvalue())
    # Log results
    logging.info(f'Converted: {file}')
    logging.info('Output:')
    logging.debug(membuffer.read())
    print('Done')


def tree2lf(tree: Path, *, test: bool = True, verbose: bool = False) -> None:
    r"""
    Change text file newline endings to LF ('\n').

    Files are only changed if the file extension matches the extension in a
    not all-inclusive set containing plaintext file extensions.

    Args:
        `tree` (Path): The top folder of a directory containing
            files to be changed.
        `test` (bool, optional): _description_. Defaults to True.
    """
    # ALl files within tree.
    files = pathwalk(tree, PLAINTEXT)
    # New files will be created in the given output folder.
    if test and not verbose:
        output_root = Path(
            input('Enter the output root folder for test files:'))
        if output_root.parts[-1] == tree.parts[-1]:
            output_root = output_root.parents[1]
        print(f'Sending files to {output_root}')
    for file in files:
        if file.suffix not in PLAINTEXT:
            continue
        if not test:  # Open file in write mode, replacing existing file.
            file2LF(file, test=test, verbose=verbose)
        else:  # Don't replace files
            if verbose:  # Print file paths that would be replaced
                file2LF(file, test=True, verbose=verbose)
            else:  # Create new files in a different folder.
                outpath = output_root / file.relative_to(tree)
                file2newLF(file, outpath, test=False, verbose=False)


if __name__ == '__main__':
    import argparse
    # Set up argparser.
    parser = argparse.ArgumentParser(
        description='Change files in the tree of the path provided to have LF'
                    ' newline endings')
    # verbose and test are mutually exclusive because test output must be
    # verbose to be a test of the results.
    parser.add_argument('-t', '--test', help='Run in test mode. If test mode'
                        ' but not verbose, asks for output file and converted'
                        ' files are sent to that folder. If verbose flag is'
                        ' used with test, no files are created.',
                        action='store_true', default=False)
    parser.add_argument('-v', '--verbose', help='Run in verbose mode.'
                        ' Prints each file path of the file being changed',
                        action='store_true', default=False)
    parser.add_argument('folder', type=str,
                        help="The path to the top folder of the tree.")
    args = parser.parse_args()
    # Handle output based on command line arguments.
    if args.test:
        print('----- Running test mode -------')
        tree2lf(Path(args.folder), test=True, verbose=args.verbose)
    else:
        tree2lf(Path(args.folder), test=False, verbose=args.verbose)
