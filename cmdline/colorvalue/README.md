# colorvalue

`colorvalue` is a command line script that returns values related to [HTML color names](https://en.wikipedia.org/wiki/Web_colors#HTML_color_names "Web colors - HTML color names | Wikipedia")

Can also be used by import within other programs.

## Usage in Terminal

```txt
py -m colorvalue -h
usage: colorvalue.py [-h] (-r | -x | -n) [-c] color [color ..]

Print the RGBA or HEX value for a given color name or the HTML color names in the given color group.

positional arguments:
  color:    For -r and -x: A string HTML color name (e.g., WhiteSmoke). Can also be written with a space. (e.g., White Smoke)
 
options:
  -h, --help  show this help message and exit.
  -r, --rgb   set return value to the color's RGB value.
  -x, --hex   set return value to the color's HEX value.
  -n, --names set return value to a tuple containg all of the HTML color names in the given color group.
  -c, --clip  send output value(s) to the clipboard.
```

### Getting HEX Value

```shell
py -m colorvalue -x WhiteSmoke
```


#### HEX to Clipboard

```shell
py -m colorvalue -x -c WhiteSmoke
```

### Getting RGB Value

```shell
py -m colorvalue -r WhiteSmoke
```

#### RGB to Clipboard

```shell
py -m colorvalue -r -c WhiteSmoke
```

### Getting Color Group Names

```shell
py -m colorvalue -n Oranges
```

#### Group Names to Clipboard

```shell
py -m colorvalue -n -c Oranges
```

## Interfaces When Importing

```python
from colorvalue import HtmlColors, get_colorvalue, get_colorgroup_names
```

### `HtmlColors().all`

Obtain the color group, name, RGB, and HEX for every HTML color name in the htmlcolors database. Returns `list[sqlite3.Row]`

```python
>>> HtmlColors().all[0]['name']
'MediumVioletRed'
>>> HtmlColors().all[0]['hex']  
'#C71585'
>>> HtmlColors().all[0]['rgb']  
'(199, 21, 133)'
```

### `HtmlColors().names`

Obtain all the HTML color names. Returns `list[str]`

```python
>>> HtmlColors().names
['AliceBlue', 'AntiqueWhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'BlanchedAlmond', 'Blue', 'BlueViolet', 'Brown', 'Burlywood', 'CadetBlue', 'Chartreuse', 'Chocolate', 'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson', 'Cyan', 'DarkBlue', 'DarkCyan', 'DarkGoldenrod', 'DarkGray', 'DarkGreen', 'DarkKhaki', 'DarkMagenta', 'DarkOliveGreen', 'DarkOrange', 'DarkOrchid', 'DarkRed', 'DarkSalmon', 'DarkSeaGreen', 'DarkSlateBlue', 'DarkSlateGray', 'DarkTurquoise', 'DarkViolet', 'DeepPink', 'DeepSkyBlue', 'DimGray', 'DodgerBlue', 'Firebrick', 'FloralWhite', 'ForestGreen', 'Fuchsia', 'Gainsboro', 'GhostWhite', 'Gold', 'Goldenrod', 'Gray', 'Green', 'GreenYellow', 'Honeydew', 'HotPink', 'IndianRed', 'Indigo', 'Ivory', 'Khaki', 'Lavender', 'LavenderBlush', 'LawnGreen', 'LemonChiffon', 'LightBlue', 'LightCoral', 'LightCyan', 'LightGoldenrodYellow', 'LightGray', 'LightGreen', 'LightPink', 'LightSalmon', 'LightSeaGreen', 'LightSkyBlue', 'LightSlateGray', 'LightSteelBlue', 'LightYellow', 'Lime', 'LimeGreen', 'Linen', 'Magenta', 'Maroon', 'MediumAquamarine', 'MediumBlue', 'MediumOrchid', 'MediumPurple', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen', 'MediumTurquoise', 'MediumVioletRed', 'MidnightBlue', 'MintCream', 'MistyRose', 'Moccasin', 'NavajoWhite', 'Navy', 'OldLace', 'Olive', 'OliveDrab', 'Orange', 'OrangeRed', 'Orchid', 'PaleGoldenrod', 'PaleGreen', 'PaleTurquoise', 'PaleVioletRed', 'PapayaWhip', 'PeachPuff', 'Peru', 'Pink', 'Plum', 'PowderBlue', 'Purple', 'Red', 'RosyBrown', 'RoyalBlue', 'SaddleBrown', 'Salmon', 'SandyBrown', 'SeaGreen', 'Seashell', 'Sienna', 'Silver', 'SkyBlue', 'SlateBlue', 'SlateGray', 'Snow', 'SpringGreen', 'SteelBlue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White', 'WhiteSmoke', 'Yellow', 'YellowGreen']
```

### `HtmlColors().groups`

Obtain all the HTML color group names.

```python
>>> HtmlColors().groups
['Pinks', 'Reds', 'Oranges', 'Yellows', 'Browns', 'Greens', 'Cyans', 'Blues', 'Purples', 'Whites', 'Blacks']
```

### `HtmlColors().map_to_name`

Obtain color_group, RGB, and HEX mapped to their HTML Color Name. Returns `dict[sqlite3.Row]`

```python
>>> HtmlColors().map_to_name['WhiteSmoke']['rgb']
'(245, 245, 245)'
```

### `HtmlColors().map_to_group`

Obtain `sqlite3.Row` for colors grouped by color_group. Returns `dict[list[sqlite3.Row]]`

```python
>>> colorvalue.HtmlColors().map_to_group['Oranges']  
[<sqlite3.Row object at 0x000002173C556A40>, <sqlite3.Row object at 0x000002173C556A10>, <sqlite3.Row object at 0x000002173C5569E0>, <sqlite3.Row object at 0x000002173C5569B0>, <sqlite3.Row object at 0x000002173C556950>]
>>> colorvalue.HtmlColors().map_to_group['Oranges'][0]['name']
'OrangeRed'
>>> colorvalue.HtmlColors().map_to_group['Oranges'][0]['rgb']
'(255, 69, 0)'
```
### `HtmlColors().colorvalue(`colorname: str, format: str`)`

Obtain an HTML color and either its RGB or HEX value. Returns `tuple[str]`.

- *color* is the HTML color name
- *format* is one of "rgb" or "hex"

```python
>>> HtmlColors().colorvalue('OrangeRed', 'rgb')
('OrangeRed', '(255, 69, 0)')
```

### `get_colorvalue(`color: str, format: str, to_clipboard: bool = False`)`

Print or copy to clipboard all color names in color_group. Returns `None`.

- *color* is the HTML color name
- *format* is one of "rgb" or "hex"
- *to_clipboard* is either `True` or `False`. Default is `False`. If `True`, the color value is copied to the clipboard. If `False`, the color value is not copied to the clipboard.

```python
>>> colorvalue.get_colorvalue('OrangeRed', 'rgb')
rgb value for "OrangeRed" is:
(255, 69, 0)
>>> colorvalue.get_colorvalue('OrangeRed', 'rgb', True) 
rgb value for "OrangeRed" is:
(255, 69, 0)
Value copied to clipboard.
```

### `get_colorgroup_names(`color_group: str, to_clipboard: bool = False`)`

Print or copy to clipboard all color names in color_group.. Returns `None`.

- *color_group* is the HTML color group name. Accepted values are Pinks, Reds, Oranges, Yellows, Browns, Greens, Cyans, Blues, Purples, Whites,  or Blacks
- *to_clipboard* is either `True` or `False`. Default is `False`. If `True`, the color value is copied to the clipboard. If `False`, the color value is not copied to the clipboard.

```python
>>> colorvalue.get_colorgroup_names('Oranges')
HTML Colors in Oranges Group:
         OrangeRed
         Tomato
         DarkOrange
         Coral
         Orange
>>> colorvalue.get_colorgroup_names('Oranges', True) 
HTML Colors in Oranges copied to clipboard.
```
