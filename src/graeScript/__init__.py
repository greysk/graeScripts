__all__ = ['path_here', 'data_path', 'logconf_path', 'logger',
           'db_block_protected_path', 'outfile_path',
           'isleap', 'mapit', '_block_protected',
           'digit_to_hex_decimal', 'digit_to_hex_binary',
           'hexadecimal_to_decimal', 'hexadecimal_to_binary',
           'binary_to_decimal', 'binary_to_hexadecimal', 'decimal_to_binary',
           'decimal_to_hexadecimal', 'to_all', 'builtin_convert',
           'to_markdown_table', 'Validator', 'String', 'Number', 'OneOf',
           'getPDFtext', 'extract_page_from_pdf', 'copy_pdf', 'rotate_right',
           'rename_file', 'delete_file', 'delete_folder', 'delete_empty_tree',
           'glob_delete', 'move_contents', 'walk_and_combine',
           'change_file_ext', 'change_file_ext_in', 'search_for',
           'found_files_to_txt', 'find_photo_folder', 'colors_to_excel',
           'getcolors', 'all_colors', 'color_names', 'colors_in_group',
           'color_value'
           ]

import logging
import logging.config
from pathlib import Path


def path_here():
    return Path(__file__).parent


def data_path():
    return path_here() / 'data'


def logconf_path():
    return data_path() / 'logging.conf'


def logger(logger_name):
    logging.config.fileConfig(path_here() / 'data/logging.conf')
    logger = logging.getLogger(logger_name)
    return logger


def db_blockprotected_path(system='win'):
    if system not in ('win', 'linux'):
        print(f'Expected "win" or "linux" got {system}')
    return data_path() / f'{system}_block_protected.db'


def outfile_path():
    out_path = Path.home() / '.pyAppOut/graeScripts'
    if (Path.home() / 'OneDrive').is_dir():
        outpath = Path.home() / 'OneDrive/.pyAppOut/graeScripts'
    out_path.mkdir(parents=True, exist_ok=True)
    return outpath
