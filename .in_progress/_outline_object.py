#! python3
"""
?? [ ] Does this add outline or make a logo??

Adds outline around foreground object.

- Foreground or background must be solid color.

How it works:
1. Makes copy of IMG_FILENAME and scans through it, pixel by pixel.
2. Checks if current pixel color == foreground (fg) or background (bg) color.
3. If color matches, checks the pixels to the top, bottom, left, and
    right of current pixel for color == fg, bg, or outline color.
4. If any of those either match OBJ_COLOR or do NOT match OUTLINE_COLOR,
    changes the current pixel color to the OUTLINE_COLOR.
5. Saves copy of IMG_FILENAME to the path set by SAVED_FILENAME.
"""
from PIL import Image
import argparse


def set_argparse():
    parser = argparse.ArgumentParser(
        description='Add outline to solid-colored object in image.')
    parser.add_argument('filename', help='A string path to the image file.')
    parser.add_argument('output_filename',
                        help='Path at which to save the output image.')
    parser.add_argument('-l', '--linecolor',
                        help=('The color to use to outline the object.'
                              ' Format as a RGBA or RGB color values.'
                              'e.g., 255,255,255,255 or 255,255,255.'),
                        default='255,255,255,255')

    exclusive = parser.add_mutually_exclusive_group(required=True)
    exclusive.add_argument('-b', '--back',
                           action='set_true',
                           help=('Use to mark `groundcolor` as being the color'
                                 'that matches the background color'
                                 ' (as opposed to matching the foreground'
                                 ' color).'))
    exclusive.add_argument('-f', '--fore',
                           action='set_true',
                           help=('Use to mark groundcolor as being the color'
                                 'that matches the foreground color'
                                 ' (as opposed to matching the background'
                                 ' color).'))
    parser.add_argument('gcolor',
                        help=('The color of the object to be outlined'
                              ' (i.e. foreground or background). Format'
                              ' as a RGBA or RGB color values.'
                              ' Ex. 0,0,0,255 or 0,0,0.'))
    # parser.add_argument('-c', '--color', action='set_true',
    # help='Makes -f|--fgcolor accept a HTML Standard Color name.')
    return parser.parse_args()

# Set up argparse to obtain information from user's command line input.
args = set_argparse()

# if args.color:
#     print('Implement')
#     raise SystemExit

# Obtain the filepath of image to be outlined.
input_image = args.filename
# Obtain the filepath for the output image.
output_filename = args.output_filename
# Properly format the RGB color values that represent the color to be used
# for the outline and the original image's fore- or back-ground color.
outline_color: tuple[int] = tuple([int(value)
                                   for value in args.outlinecolor.split(',')])
groundcolor: tuple[int] = tuple([int(value)
                                 for value in args.gcolor.split(',')])

# Create a copy of the original image.
org_image = Image.open(input_image).copy()
# Obtain the width and height of the image.
width, height = org_image.size

# Outline image by checking, for each pixel, whether it lies at the boarder line between the fore- or back-ground color and the rest of the image.
for x in range(width):  # ➡
    for y in range(height):  # ⬇
        current_pixel_coord = (x, y)
        current_pixel_color = org_image.getpixel(current_pixel_coord)
        # Set coordinates for adjacent pixels.
        top_bot_left_right = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
        # Holds results of test run on adjacent pixels for each pixel.
        test_adjacent = []
        # Check current pixel and skip if matches groundcolor.  We are
        #  outlining groundcolor not overwriting it.
        if current_pixel_color == groundcolor:
            continue
        for adjacent_coordinate in top_bot_left_right:
            # Handle if adjacent pixel is out of bounds.
            try:
                adjacent = org_image.getpixel(adjacent_coordinate)
            except IndexError:
                continue
            # An adjacent pixel passes the test when ground color is the foreground color if it is the same as the foreground color or if an adjacent pixel does not match the outline color.
            else:
                if args.fore:
                    # If adjacent is not part of the outline and is part of the foreground, we're at the boarderline between the background of the image and the foreground.
                    if adjacent != groundcolor or adjacent == outline_color:
                        # Doesn't pass if adjacent does not match foreground color or if it matches outline color.
                        continue

                else:
                    if adjacent == groundcolor or adjacent == outline_color:
                        # Doesn't pass if adjacent matches background color or adjacent matches outline color.
                        continue
                test_adjacent.append(adjacent_coordinate)
        # If any of the adjacent pixels pass the test, the current pixel is
        # at the borderline, change current pixel to outline color.
        if test_adjacent:
            org_image.putpixel(current_pixel_coord, outline_color)

org_image.save(output_filename)
