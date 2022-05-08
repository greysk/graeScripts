# graeScript

This is a package containing various programs written for my own personal use and for learning purposed.

> **WARNING**: This is very much a work in progress. There are no guarantees of reliability. In fact, I guarantee that I will make changes to the code within this that will utterly change how anything and everything within here could be used, and I do so frequently. If you would like to use code within here, feel free to do so, but I would highly recommend forking this repo and being very careful about pulling any changes from here into your fork.

## Currently this repository contains two, separate groups of code:

1. A couple of small, command line scripts found in the [cmdline folder](cmdline) that were written to be run using batch files and Windows run application.
2. A Python package called [`graeScript`](src/graeScript) which contains a mess of small, mostly unrelated scripts that I've written. It was made to ease reuse of these scripts easier for myself and to create a central location for them.

# Details of small, independent scripts in [cmdline](cmdline) dir

|Filename     |Dependencies|Summary|
|-------------|------------|-------|
|**colorvalue.py**|[pyperclip](https://pypi.org/project/pyperclip/)\* and [graeScripts.Drawing](src/graeScript/Drawing) |Returns/copies to the clipboard either the RGB or the Hex color values of a given [HTML color name](https://www.w3schools.com/colors/colors_names.asp).|
|**CRLF_to_LF.py**||Convert plain text files in a directory tree to have LF newline endings.|
|**pf_fix_path_sep.py**|[pyperclip](https://pypi.org/project/pyperclip/)|Takes path from clipboard, replaces `\` path separators with `/`, and copies new string to clipboard.|
|**zipdir**||Creates a zipfile containing the folders and files within a directory tree.|

*\*Code can be altered relatively easily to remove dependency.*

# Details of [`src/graeScript`](src/graeScript)

*Writing of the details is a work-in-progress.*
*Last edit: 2022-02-11*

## [`htmlcolors.py`](src/graeScript/htmlcolors.py)

Created to simplify obtaining the HEX and RGB value for the [HTML Color Names](https://www.w3schools.com/colors/colors_names.asp). Additions were later made to simplify obtaining all HTML color names and finding a desired color name by color group.

- Requires [Pyperclip](https://pypi.org/project/pyperclip/)

### [`str_rgb_to_tuple()`](src/graeScript/htmlcolors.py#L9) -> Tuple

Get a tuple from a string RGB value.

Arg:

- *s*: str

### [*class* `HtmlColors`](src/graeScript/htmlcolors.py#L12)

Return values related to all HTML Color Names.

### *HtmlColors.*[`all`](src/graeScript/htmlcolors.py#L34) -> list[sqlite4.Row]

Return the color group, name, RGB value, and Hex values for every HTML color name.

### *HtmlColors.*[`names`](src/graeScript/htmlcolors.py#L62) -> list[str]

Return all HTML color names.

### *HtmlColors.*[`map_to_name`](src/graeScript/htmlcolors.py#L71) -> dict[sqlite3.Row]

Map `HtmlColors.all` to the HTML color names.

### *HtmlColors.*[`map_to_group`](src/graeScript/htmlcolors.py#L85) -> dict[list[sqlite3.Row]]

Map `HtmlColors.all` to the HTML color names.

### [`color_value()`](src/graeScript/htmlcolors.py#L111) -> tuple[str]

The first item in tuple is properly formatted HTML color name, and the second item is the color's RGB or HEX value depending on *format*.

Args:

- *format*: str
- *colorname*: str

### [`get_colorvalue()`](src/graeScript/htmlcolors.py#L142) -> None

Prints or copies to clipboard the properly formatted HTML color name *color*, and the color's RGB or HEX value depending on *format*.

- Requires [Pyperclip](https://pypi.org/project/pyperclip/)

Args:

- *color*: str
- *format*: str
- *to_clipboard*: bool = `False`

If *to_clipboard* is `True`, the RGB/HEX value is also copied to the clipboard.

### [`get_group_colornames()`](src/graeScript/htmlcolors.py#L168) -> None

Print or copy to the clipboard all HTML color names in *color_group*.

- Requires [Pyperclip](https://pypi.org/project/pyperclip/)

Args:

- *color_group*: str
- *to_clipboard*: bool = `False`

## [`file_explorer/delete_move_dirs.py`](src/graeScript/file_explorer/delete_move_dirs.py)

A collection of functions related to moving and deleting files and folders. Initially was one function to merge folders within a directory tree, but was refactored into this. Still somewhat a work-in-progress.

All file-changing functions print the changes made.

All file-changing functions have a parameter called '*test*', that defaults to `True` and causes the function to make no file changes.

### [`rename_file()`](src/graeScript/file_explorer/delete_move_dirs.py#L222) -> None

Rename *source* file to *destination* file.

Args:

- *source*: Path | str
- *destination*: Path
- *test*: bool = `True`

### [`delete_file()`](src/graeScript/file_explorer/delete_move_dirs.py#L244) -> None

Deletes *file*.

Args:

- *file*: Path | str
- *test*: bool = `True`

### [`delete_folder()`](src/graeScript/file_explorer/delete_move_dirs.py#L264) -> None

Deletes *dir* if it is empty.

Args:

- *dir*: Path | str
- *test*: bool = `True`

### [`delete_empty_tree()`](src/graeScript/file_explorer/delete_move_dirs.py#L292) -> None

Deletes empty folders within directory's tree.

Args:

- *dir*: Path | str
- *test*: bool = `True`

Prints changes made

### [`glob_delete()`](src/graeScript/file_explorer/delete_move_dirs.py#L315) -> None

Deletes files in directory *dir* based on the glob pattern in *glob_pattern*.

Args:

- *dir*: Path | str
- *glob_pattern*: str
- *test*: bool = `True`

### [`move_contents()`](src/graeScript/file_explorer/delete_move_dirs.py#L240) -> list[dict]

Move all of *source* directory's contents into *destination*.

Args:

- *source*: Path | str
- *destination*: Path
- *test*: bool = `True`
- *\*args*: str

*\*args* takes either 'replace', 'delete', 'compare', or None which dictates how move conflicts will be handled.

- 'replace': replace file in *destination* with the conflicting one from *source*
- 'delete': delete file in *source*
- 'compare': compares the last edit date of the files in conflict, keeping whichever has the most recent date. (Either moves or deletes *source*)
- If no argument is passed for *\*args*, this function returns details about files that weren't moved and their matching destination file.

### [`_walk_and_combine()`](src/graeScript/file_explorer/delete_move_dirs.py#L420) -> None

In *start_dir*, combine folders when there is a 2 similar folders, 1 matching *destination_pattern*' and another matching folder1's `match.group(match_group_num)`.

For example, if you have a folder full of music organized *music/<artist>/<album>* in which some artist have duplicate album folders with different, but similar names. (For example, *music/Real Artist/1996 - MTV Unplugged (live)* and *music/Real Artist/MTV Unplugged*.) This would merge any similar folders found in each *album/* directory.

- Leading underscore because hasn't been run/tested since parts of it were refactored into functions listed above.

Args:

- *start_dir*: Path | str
- *dest_pattern*: str
- *match_group_num*: int
- *test*: bool = `True`
- *\*args*: str

Continuing above example:

```python
_walk_and_combine(start_dir='music', dest_pattern=r'(\d{2,4} - )(.*)( live)', match_group=1, test=False)
```

For every artist folder in music, this function:

1. looks for an album folder that matches the entire regex in *destination_pattern* (we'll call this folder `destination`),
2. looks for an album folder matching `destination`'s `match.group(1)` (we'll call this folder `source`),
3. if both are found, the fucntion moves the files from `source` into `destination`, using *\*args* to determine how to handle conflicts, and
5. if `source` is empty after the move, the function deletes the `source` folder.

*\*args* takes either 'replace', 'delete', 'compare', or None which dictates how move conflicts will be handled.

- 'replace': replace file in *destination* with the conflicting one from *start_dir*
- 'delete': delete file in *start_dir*
- 'compare': compares the last edit date of the files in conflict, keeping whichever has the most recent date. (Either moves or deletes *start_dir*)
- If no argument is passed for *\*args*, then any conflict files will not be moved.

## [`file_explorer/edit_filename.py`](src/graeScript/file_explorer/edit_filename.py)

Edit a given file name or file names in a given directory / directory tree.

### [`change_file_ext()`](src/graeScript/file_explorer/edit_filename.py#L6) -> None

Rename *file* by replacing it's existing extension with *new_ext*.

Args:

- *file*: Path | str
- *new_ext*: str
- *Test*: bool = `True`

### [`change_file_ext_in()`](src/graeScript/file_explorer/edit_filename.py#L14) -> None`

Rename files in *dir* by replacing their existing extension with *new_ext*.

Args:

- *dir*: Path | str
- *new_ext*: str
- *replace_ext*: str = `'*.*'`
- *Test*: bool = `True`

If *replace_ext* is uses, then only the files with *replace_ext* will be renamed

## [`file_explorer/find_files.py`](src/graeScript/file_explorer/find_files.py)

Search computer for certain files.

### [`search_for()`](src/graeScript/file_explorer/find_files.py#L7) -> list[Path]

Search the directory tree `dir` and returns files matching `glob`.

Args:

- *dir*: Path | str
- *glob*: Path | str


### [`found_files_to_text()`](src/graeScript/file_explorer/find_files.py#L29) -> list[Path]

Call `search_for()` and output found file paths to `txt_file`.

Args:

- *dir*: Path | str
- *glob*: Path | str
- *txt_file*: Path | str

## [`file_explorer/find_folders.py`](src/graeScript/file_explorer/find_folders.py)

Search computer for certain folders.

- Requires [Pillow](https://pypi.org/project/Pillow/)

### [`find_photo_folder()`](src/graeScript/file_explorer/find_photo_folder.py#L12) -> None

Searches computer directory for picture folders.

Args:

- *start_dir*: str

From [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) by Al Sweigart [Chapter 17](https://automatetheboringstuff.com/chapter17/#calibre_link-3617)

## [`markdown/to_md_list.py`](src/graeScript/markdown/to_md_list.py)

From input text, output a markdown list.

- Requires [Pyperclip](https://pypi.org/project/pyperclip/)

### [`bullet_list()`](src/graeScript/markdown/to_md_list.py#L19) -> list

Create a markdown bulleted list from *text*.

Args:

- *text*: str
- *as_todo*: bool = `False`

If *as_todo* is `True`, bullets are written as `'- [ ]'` instead of `'-'`.

Determines list items and level by number of spaces of indentation.

### [`from_clipboard()`](src/graeScript/markdown/to_md_list.py#L63) -> None

Uses `bullet_list`, taking *text* from clipboard.

Args:

- *text*: str
- *as_todo*: bool = `False`

- Requires [Pyperclip](https://pypi.org/project/pyperclip/)

## [`markdown/to_md_table.py`](src/graeScript/markdown/to_md_table.py)

From input text, print out a markdown table.

### [`table()`](src/graeScript/markdown/to_md_table.py#L105) -> None

Prints a markdown table of *rows*.

Args:

- *rows*: list | tuple
- *align*: str = `'l'`
- *center_header*: bool = `True`
- *col_padding*: int = `0`
- *header_row*: list = `[]`

## [`PDFiles/create_pdfs`](src/graeScript/PDFiles/create_pdfs.py)

Create PDFs from existing PDFs.

- Requires [PyPDF2](https://pypi.org/project/PyPDF2/)

## [`PDFiles/getPDFtext.py`](src/graeScript/PDFiles/getPDFtext.py)

Obtain the text from a PDF.

- Requires [PyMuPDF](https://pypi.org/project/PyMuPDF/)

## [`utils/convert_nums.py`](src/graeScript/utils/convert_nums.py)

Functions related to converting numbers from one base to other base(s).

### [`get_decimal()`](src/graeScript/utils/convert_nums.py#L18) -> int

Convert a decimal, binary, hexadecimal, or octal to an integer.

Args:

- *digit*: int | str

### [`builtin_convert()`](src/graeScript/utils/convert_nums.py#L42) -> list

Obtain decimal, hexadecimal, and binary value for an integer decimal.

Args:

- *digit*: int | str
- *include_prefix*: bool = `False`
- *hex_case*=`str.upper`

### [`numbers_to_md_table()`](src/graeScript/utils/convert_nums.py#L92) -> None

Prints markdown number conversion table from *start_num* through *stop_num*.

Args:

- *start_num*: int | str
- *stop_num*: int | str
- *include_prefix*: bool = `False`

## [`utils/isleap`](src/graeScript/utils/isleap.py)

Can be used in terminal `py isleap.py <year>` and prints message to inform if *year* is a leap year or not.

### [`isleap()`](src/graeScript/utils/isleap.py#L8) -> Bool

Returns `True` if *year* entered is a leap year.

Args:

- *year*: int

## [`utils/mergetxt.py`](src/graeScript/utils/mergetxt.py)

Merge text files.

### [`mergetext()`](src/graeScript/utils/mergetxt.py#L3) -> set

Merge two text files in which each line contains one word. (Made to merge CSpell dictionary text files).

Args:

- *file1*: str
- *file2*: str

## [`utils/validation.py`](src/graeScript/utils/validation.py)

Several classes for validating class attribute values.

From [Python Documentation: HOWTO Descriptors](https://docs.python.org/3/howto/descriptor.html#validator-class)

### *class* `Validator`

> A validator is a descriptor for managed attribute access. Prior to storing any data, it verifies that the new value meets various type and range restrictions. If those restrictions aren't met, it raises an exception to prevent data corruption at its source. - [PyDocs](https://docs.python.org/3/howto/descriptor.html#validator-class)

### *class* `String(Validator)`

> `String` verifies that a value is a str. Optionally, it validates a given minimum or maximum length. It can validate a user-defined predicate as well. - [PyDocs](https://docs.python.org/3/howto/descriptor.html#custom-validators)

### *class* `Number(Validator)`

> `Number` verifies that a value is either an int or float. Optionally, it verifies that a value is between a given minimum or maximum. - [PyDocs](https://docs.python.org/3/howto/descriptor.html#custom-validators)

### *class* `OneOf(Validator)`

> `OneOf` verifies that a value is one of a restricted set of options." - [PyDocs](https://docs.python.org/3/howto/descriptor.html#custom-validators)
