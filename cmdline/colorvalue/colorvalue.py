#! python3
"""Returns the RGB or HEX value for a given HTML standard color name.

To remove pyperclip dependency, comment out line 13 and line 132.

Usage:
    myGetColor.py RGB|HEX Color[ ]Name
"""
import argparse
import csv
from pathlib import Path

import pyperclip

# CSV file containing HTML standard color names and their RGB and HEX values.
COLORS_CSV: Path = Path(__file__).parent / 'html_colors.csv'

# Obtain dictionary with key of HtmlColorName and value of colorformat.
with open(COLORS_CSV, newline='') as f:
    dictreader = csv.DictReader(f)
    ALL_COLORS: dict = {row['Name']: {'HEX': row['HEX'], 'RGB': row['RGB']}
                        for row in dictreader}


def colorname(htmlcolor: str) -> str:
    """Format htmlcolor to better match standard HTML color name."""
    if len(htmlcolor) > 1:
        return ''.join([name.title() for name in htmlcolor])
    else:
        return htmlcolor[0]


def color_value(value_format: str, colorname: str) -> tuple[str]:
    """
    Test htmlcolor and tries to return the HTML color and it's value.

    Args:
        value_format (str, optional):
            'RGB' or 'HEX'. Defaults to colorformat.
        htmlcolor (str, optional):
            HTML color name. Defaults to args.htmlcolor.

    Raises:
        SystemExit: If htmlcolor is not found in the HTML Standard Colors.

    Returns:
        tuple[str]: Tuple of HtmlStandardColorName and its RGB or HEX value.
    """
    def test_colorname(name: str = colorname, tries: int = 1) -> tuple[str]:
        """
        Tests whether name provided is in HTML standard color names.

        Args:
            name (str, optional): The name to test. Defaults to colorname.
            tries (int, optional): Number of tries. Defaults to 1.

        Raises:
            SystemExit: If tries is greater than 2.

        Returns:
            tuple[str] : The HtmlStandardColorName and its RGB or HEX value.
        """
        original_colors: tuple = tuple(ALL_COLORS.keys())
        lower_colors: tuple = tuple([color.lower()
                                     for color in ALL_COLORS.keys()])
        if tries > 2:
            print(f'"{colorname}" not found in HTML standard colors.')
            print('Program exiting...')
            raise SystemExit
        try:
            ALL_COLORS[name][value_format]
        except KeyError:
            if name.lower() in lower_colors:
                index: int = lower_colors.index(name.lower())
                name: str = original_colors[index]
                test_colorname(name, 2)
            else:
                test_colorname(name, 100)
        return (name, ALL_COLORS[name][value_format])
    return test_colorname()


if __name__ == '__main__':
    # Set up argparse to obtain user input from the command line (CLI).
    parser = argparse.ArgumentParser(description=(
        'Usage: {--rgb|--hex} {HtmlColor|html color|Htmlcolor}.'
        ' Sends to clipboard and prints the RGB/HEX color given HTML'
        ' standard color name. In RGBA, all HTML standard colors have'
        ' an A of 255; if want RGBA color, append "255" to the RGB value.')
    )
    # Add mutually-exclusive group to select output of either rgb or hex value.
    exclusive_group = parser.add_mutually_exclusive_group(required=True)
    exclusive_group.add_argument('-r', '--rgb',
                                 action='store_true',
                                 help='Sets return value to RGB value.')
    exclusive_group.add_argument('-x', '--hex',
                                 action='store_true',
                                 help='Sets return value to HEX value.')
    # Add the HTML string color name argument.
    parser.add_argument(
        'htmlcolor',
        help=('A string color name.'
              ' Two-word color names can be written as two words,'
              ' otherwise they must be written with proper case.'
              ' For example, "WhiteSmoke" can be written as "WhiteSmoke",'
              ' "white smoke", "White smoke", "WHITE SMOKE", etc.'),
        nargs='+')

    # Obtain args from command line.
    args = parser.parse_args()

    # Determine whether the output should be in RGB or Hex format.
    def color_format(args=args):
        """Define colorformat from CLI using exclusive_group."""
        if args.hex:
            return 'HEX'
        elif args.rgb:
            return 'RGB'
        else:
            print('Color format must be set using either the flag'
                  ' for RGB (-r|--rgb) or the flags for'
                  ' HEX (-x|--hex). Exiting')
            raise SystemExit
    colorformat: str = color_format()

    # Obtain the HTML string color name
    htmlcolor: str = args.htmlcolor
    # Obtain the properly-formatted string color name and the RGB/Hex value.
    color_name, colorvalue = color_value(value_format=colorformat,
                                         colorname=colorname(htmlcolor))
    # Copy color value to the clipboard
    pyperclip.copy(colorvalue)
    # Print information about requested color format, proper colorname,
    # and the resulting color value.
    print(f'{colorformat} value for "{color_name}" copied to clipboard.'
          ' Value is:')
    print(f'{colorvalue}')
