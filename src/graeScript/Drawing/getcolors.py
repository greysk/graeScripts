#! python3
"""Returns the RGB or HEX value for a given HTML standard color name.

Usage:
    myGetColor.py RGB|HEX Color Name
"""
import argparse
import csv

import pyperclip

from graeScript import data_path


def all_colors() -> dict:
    """Returns dictionary of colornameName and value of colorformats"""
    colors_csv = data_path() / 'html_colors.csv'
    with open(colors_csv, newline='') as f:
        dictreader = csv.DictReader(f)
        all_colors = {row['Name']: {'HEX': row['HEX'], 'RGB': row['RGB'],
                                    'Group': row['Group']}
                      for row in dictreader}
    return all_colors


def color_names() -> tuple:
    """Returns all HTML color names"""
    return tuple(all_colors().keys())


def colors_in_group(color_group: str) -> list[str]:
    """
    Returns the HTML color names in color_group such as "Pinks".

    Args:
        color_group (string): A color group. (e.g., "Pinks", "Reds")

    Returns:
        list: A list of all HTML color names in color_group.
    """
    colors = all_colors()
    return [color for color in colors.keys()
            if colors[color]['Group'] == color_group]


def color_value(
        value_format: str, colorname: str) -> tuple[str, tuple[int, int, int]]:
    """
    Tests colorname and tries to return the HTML color and it's value_format.

    Args:
        value_format (str, optional): 'RGB' or 'HEX'.
        colorname (str, optional): HTML color name.

    Raises:
        SystemExit: If colorname is not found in the HTML Standard Colors.

    Returns:
        tuple[str, tuple[int, int, int]]:
                THtmlStandardColorName and its RGB or HEX value.
    """
    def test_colorname(
            name: str = colorname, attempt: int = 1
            ) -> tuple[str, tuple[int, int, int]]:
        """
        Tests whether name provided is in HTML standard color names.

        Args:
            name (str, optional): The name to test. Defaults to colorname.
            tries (int, optional): Number of tries. Defaults to 1.

        Raises:
            SystemExit: Raised if tries is greater than 2.

        Returns:
            tuple[str, tuple[int, int, int]]:
                THtmlStandardColorName and its RGB or HEX value.
        """
        ALL_COLORS = all_colors()
        original_colors = color_names()
        lower_colors = frozenset([color.lower() for color in original_colors])
        if attempt > 2:
            print(f'"{colorname}" not found in HTML standard colors.')
            print('Program exiting...')
            raise SystemExit
        try:
            ALL_COLORS[name][value_format]
        except KeyError:
            if name.lower() in lower_colors:
                index = lower_colors.index(name.lower())
                name = original_colors[index]
                test_colorname(name, 2)
            else:
                test_colorname(name, 100)
        return name, ALL_COLORS[name][value_format]
    return test_colorname()


if __name__ == '__main__':
    # Set up argparse for command line interface (CLI).
    summary = (
        """Usage: {--rgb|--hex|--names} color.
        Copies and prints the RGB or HEX value for a given color name, or
        if --names flag is used, prints HTML color names in given color group.

        To make an RGB format to RGBA, append "255" to the RGB value.
        """
        )
    color_name_help = (
        """For flags --rgb, -r, --hex, and -x:
            A string HTML color name. (ex. WhiteSmoke)
        For flags --names and -n:
            An HTML color group. (ex. Pinks)
        """
        )
    parser = argparse.ArgumentParser(description=summary)
    exclusive_group = parser.add_mutually_exclusive_group(required=True)
    exclusive_group.add_argument('-r', '--rgb',
                                 action='store_true',
                                 help='Sets return value to RGB value.')
    exclusive_group.add_argument('-x', '--hex',
                                 action='store_true',
                                 help='Sets return value to HEX value.')
    exclusive_group.add_argument('-n', '--names',
                                 action='store_true',
                                 help='Sets return value to tuple containing'
                                 ' all HTML standard color names.')
    parser.add_argument('color', help=color_name_help, nargs='+')
    args = parser.parse_args()

    def colorformat(args=args):
        """Define color format from command line interface."""
        if args.hex:
            return 'HEX'
        elif args.rgb:
            return 'RGB'
        elif args.names:
            return 'Names'
        else:
            print(
                'Color format must be set using either the flags for'
                ' RGB (-r|--rgb), HEX (-x|--hex), or Color Names (-n|--names).'
                ' Exiting')
            raise SystemExit

    format = colorformat(args)
    color = args.color
    if format == 'Names':
        print(f'HTML Colors in {color.upper()} Group:')
        for name in colors_in_group(color.upper()):
            print('\t', name)
    else:
        color = ''.join(color)
        color_name, output = color_value(value_format=format,
                                         colorname=color)
        pyperclip.copy(output)
        print(f'{format} value for "{color_name}" copied to clipboard.'
              ' Value is:')
        print(f'{output}')
