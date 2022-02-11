__all__ = ['path_here', 'data_path', 'logconf_path', 'logger',
           'db_block_protected_path', 'outfile_path',
           'HtmlColors', 'color_value', 'get_colorvalue',
           'get_group_colornames', 'rename_file', 'delete_file',
           'delete_folder', 'delete_empty_tree', 'glob_delete',
           'move_contents', 'change_file_ext', 'change_file_ext_in',
           'search_for', 'found_files_to_text', 'find_photo_folder'
           # [ ] Finish adding
           ]

import logging
import logging.config
from pathlib import Path


def path_here() -> Path:
    """Path to graeScript cwd ('graeScript/')"""
    return Path(__file__).parent


def data_path() -> Path:
    """Path to data directory ('graeScript/data')."""
    return path_here() / 'data'


def logconf_path() -> Path:
    """Path to logging configuration"""
    return data_path() / 'logging.conf'


def logger(logger_name: str) -> logging.Logger:
    """Basic logger for graeScripts"""
    logging.config.fileConfig(path_here() / 'data/logging.conf')
    logger = logging.getLogger(logger_name)
    return logger


def db_blockprotected_path(system='win') -> Path:
    """Path to {system}_block_protected.db"""
    if system not in ('win', 'linux'):
        print(f'Expected "win" or "linux" got {system}')
    return data_path() / f'{system}_block_protected.db'


def outfile_path() -> Path:
    """Path to directory for output files. Created if doesn't exist.

    If OneDrive is set up, outfile_path is in OneDrive. Otherwise,
    it is in the home directory. Relative path: '.pyAppOut/graeScript'.
    """
    outpath = Path.home() / '.pyAppOut/graeScript'
    if (Path.home() / 'OneDrive').is_dir():
        outpath = Path.home() / 'OneDrive/.pyAppOut/graeScript'
    outpath.mkdir(parents=True, exist_ok=True)
    return outpath
