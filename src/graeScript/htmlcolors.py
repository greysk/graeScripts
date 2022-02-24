"""Obtain HTML color names, groups, RGB, and HEX values.

Author: Graeson Thomas
Last Modified: 2022-02-20
"""

import sqlite3
from pathlib import Path

_DB: Path = Path(__file__).parent / 'data/htmlcolors.db'

# [ ] Add feature to display color(s) using Pillow (in another file)


def str_rgb_to_tuple(s: str) -> tuple:
    """Get a tuple from a string RGB value.

    Example:
    >>> rgb_str = '(255, 255, 255)'
    >>> print(type(rgb_str))
    <class 'str'>
    >>> rgb_tuple = str_rgb_to_tuple(rgb_str)
    >>> rgb_tuple
    (255, 255, 255)
    >>> type(rgb_tuple)
    <class 'tuple'>
    """
    i1, i2, i3 = [int(i) for i in s.strip('()').split(', ')]
    return i1, i2, i3


class HtmlColors:
    def __init__(self) -> None:
        """Obtain values related to all HTML color names in various formats.

        HTML color names: https://www.w3schools.com/colors/colors_names.asp

        Available data for each color includes:
            HTML color names,
            color groups,
            RGB value,
            HEX value
        """
        # Set up html_colors database using schema.sql
        if not _DB.exists():
            _conn = sqlite3.connect(_DB)
            with open(Path(__file__).parent / 'data/htmlcolors_schema.sql',
                      mode='r') as f:
                _conn.executescript(f.read())
            _conn.commit()
            _conn.close()

    @property
    def all(self) -> list[sqlite3.Row]:
        """
        Obtain the color group, name, RGB, and HEX for every HTML color name.

        Items in `sqlite3.Row` objects can be accessed both by index (like
        tuples) and by case-insensitive column name (similar to dictionaries).
        Also like dictionaries, column names can be obtained using the method
        `keys()`
            https://docs.python.org/3/library/sqlite3.html#sqlite3.Row

        Returns:
            list[sqlite3.Row]: Each item contains data for one color.
        """
        conn = sqlite3.connect(_DB, detect_types=sqlite3.PARSE_COLNAMES)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('''SELECT
                        groupname AS color_group,
                        colorname AS name,
                        rgb AS RGB,
                        hex AS HEX
                    FROM
                        htmlcolors
                    LEFT JOIN colorgroups
                        ON group_id = colorgroups.rowid;''')
        return cur.fetchall()

    @property
    def names(self) -> list[str]:
        "Obtain all HTML Color names"
        conn = sqlite3.connect(_DB)
        cur = conn.execute('SELECT colorname FROM htmlcolors;')
        colornames = [i[0] for i in cur.fetchall()]
        conn.close()
        return colornames

    @property
    def map_to_name(self) -> dict[sqlite3.Row]:
        """
        Obtain color_group, RGB, and HEX mapped to their HTML Color Name.

        Returns:
            dict: Keys are HTML color names and values is dictionary of
                  the color's color_group, RGB and HEX value.
        """
        # Obtain html colors from database
        rows = self.all()
        # Obtain list of column names excluding by_column_name
        return {row['name']: row for row in rows}

    @property
    def map_to_group(self) -> dict[list[sqlite3.Row]]:
        """
        Obtain `sqlite3.Row` for colors grouped by color_group.

        Items in `sqlite3.Row` objects can be accessed both by index (like
        tuples) and by case-insensitive column name (similar to dictionaries).
        Also like dictionaries, column names can be obtained using the method
        `keys()`
            https://docs.python.org/3/library/sqlite3.html#sqlite3.Row

        Returns:
            dict[list]: Keys are color_groups whose value is a
                list of `sqlite3.Row`s of HTML colors in that color_group
        """
        # Obtain html colors from database
        conn = sqlite3.connect(_DB)
        cur = conn.execute('SELECT * FROM colorgroups;')
        groups = cur.fetchall()
        conn.close()
        groups.sort()
        rows = self.all
        return {group[0]: [row for row in rows
                           if row['color_group'] == group[0]]
                for group in groups}


def color_value(format: str, colorname: str) -> tuple[str]:
    """
    Obtain an HTML color and either it's RGB or HEX value.

    Args:
        `format` (str, optional): 'RGB' or 'HEX'.
        `colorname` (str, optional): HTML color name.

    Raises:
        `SystemExit`: When colorname is not found in the HTML Standard Colors.

    Returns:
        tuple[str]:
            The HTML standard color name and it's rgb or hex value as a string.
    """
    color_rows = HtmlColors().all
    color_names = HtmlColors().names
    if ' ' in colorname:
        colorname = ''.join([i.title() for i in colorname.split(' ')])
    if colorname not in color_names:
        corrected = [color for color in color_names
                     if color.lower() == colorname.lower()]
        try:
            corrected[0]
        except IndexError:
            print(f'"{colorname}" not in HTML standard colors.')
            raise SystemExit
    color_row = [row for row in color_rows if row['name'] == colorname][0]
    return (colorname, color_row[format])


def get_colorvalue(color: str, format: str, to_clipboard: bool = False
                   ) -> None:
    """
    Print or copy to clipboard either the hex or rgb value for color.

    If `to_clipboard` is true, `pyperclip` module is required.

    Args:
        `color` (str|list): The HTML color name for which to get value.
        `format` (str): Either rgb or hex. The value to be returned.
        `to_clipboard` (bool, optional): If True, values are sent to clipboard.
                                    Defaults to False.
    """
    # Join with space between args - Color value handles formatting.
    color_name, rgb_or_hex = color_value(format, color)
    # Print values to terminals
    print(f'{format} value for "{color_name}" is:')
    print(f'{rgb_or_hex}')
    # Send rgb or hex value to clipboard.
    if to_clipboard:
        import pyperclip
        pyperclip.copy(rgb_or_hex)
        print('Value copied to clipboard.')
    return None


def get_group_colornames(color_group: str, to_clipboard: bool = False) -> None:
    """
    Print or copy to clipboard all color names in color_group.

    If `to_clipboard` is true, `pyperclip` module is required.

    Args:
        `color_group` (str): The color group (e.g., 'Pinks').
        `to_clipboard` (bool, optional): If True, values are sent to clipboard.
                                       Defaults to False.
    """
    # Obtain HTML color names in color_group.
    colors = [row['name'] for row in HtmlColors().map_to_group[color_group]]
    # Print HTML colors to terminal with each on own line.
    if not to_clipboard:
        print(f'HTML Colors in {color_group} Group:')
        for name in colors:
            print('\t', name)
    # Send color names to clipboard with each name on own line.
    else:
        import pyperclip
        color_names = '\n'.join(colors)
        pyperclip.copy(color_names)
        print(f'HTML Colors in {color_group} copied to clipboard.')
    return None
