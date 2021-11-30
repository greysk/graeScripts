__all__ = (
    'delete_move_dirs',
    'find_duplicate_files',
    'find_photo_folder',
    'colorsToExcel',
    'getcolors',
    'isleap',
    'mapIt',
    'add_blocked_dirs',
    )

import logging
import logging.config
from pathlib import Path

pkg_init_dir = Path(__file__).parent
to_data_folder = pkg_init_dir / 'data'
to_logging_config = pkg_init_dir / 'data/logging.conf'
win_block_protected = to_data_folder / 'win_block_protected.db'
linux_block_protected = to_data_folder / 'linux_block_protected.db'
if (Path.home() / 'OneDrive').is_dir():
    shared_out_dir = Path.home() / 'OneDrive/_pyApps/graeScripts'
else:
    shared_out_dir = Path.home() / '_pyApps/graeScripts'
if not shared_out_dir.is_dir():
    shared_out_dir.mkdir(parents=True, exist_ok=True)

logging.config.fileConfig(pkg_init_dir / 'data/logging.conf')
logger = logging.getLogger('graescript')
