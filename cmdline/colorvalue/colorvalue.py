#! python3
"""Returns the RGB or HEX value for a given HTML standard color name.

To remove pyperclip dependency, comment out line 13 and line 132.

Usage:
    myGetColor.py RGB|HEX Color[ ]Name
"""
import argparse

from graeScript.htmlcolors import get_group_colornames, get_colorvalue

# Create parser for argparser.
parser = argparse.ArgumentParser(description=(
    """Usage: {--rgb|--hex|--names} color.
    Copies and prints the RGB or HEX value for a given color name, or
    if --names flag is used, prints HTML color names in given color group.

    To make an RGB format to RGBA, append "255" to the RGB value.
    """
    ))
# Create mutually exclusive group. Options are one of:  rgb, hex, or names.
exclusive_group = parser.add_mutually_exclusive_group(required=True)
exclusive_group.add_argument('-r', '--rgb',
                             action='store_true',
                             help='Sets return value to RGB value.')
exclusive_group.add_argument('-x', '--hex',
                             action='store_true',
                             help='Sets return value to HEX value.')
exclusive_group.add_argument('-n', '--names',
                             action='store_true',
                             help='Sets return value to tuple containing all'
                             ' of the HTML standard color names in the given'
                             ' names color group.')

# Add send to clipboard flag which is optional.
parser.add_argument('-c', '--clip',
                    action='store_true',
                    help='Send output value(s) to clipboard.')

# Add argument for the color/group color name.
parser.add_argument('color', nargs='+', help=(
    """
    For flags --rgb, -r, --hex, and -x:
        A string HTML color name. (ex. WhiteSmoke)
    For flags --names and -n:
        An HTML color group. (ex. Pinks)
    """
    ))


if __name__ == '__main__':
    # Get arguments as a namespace from command line.
    args = parser.parse_args()

    if args.names:
        # Get HTML color names based on color group.
        get_group_colornames(''.join(args.color), args.clip)
    else:
        # Get either RGB or HEX values for HTML color matching color.
        get_colorvalue(' '.join(args.color), 'rgb' if args.rgb else 'hex',
                       args.clip)
