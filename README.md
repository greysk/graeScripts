# graeScript

This is a package containing various programs written for my own personal use and for learning purposed.

**WARNING**: This is very much a work in progress. There are no guarantees of reliability. In fact, I guarantee that I will make changes to the code within this that will utterly change how anything and everything within here could be used, and I do so frequently. If you would like to use code within here, feel free to do so, but I would highly recommend forking this repo and being very careful about pulling any changes from here into your fork.

Currently this repository contains two, separate groups of code:

1. A couple of small, independent scripts written to be run using Windows run application using batch files. (Found in the [cmdline folder](cmdline).)
2. A Python package called `graeScript` which contains a mess of small, mostly unrelated scripts that I've written. It's primary purpoase was making reuse of these scripts easier for myself and to create a central location for them.

## Details of small, independent scripts in [cmdline](cmdline) dir

|Filename     |Dependencies|Summary|
|-------------|------------|-------|
|**colorvalue.py**|[pyperclip](https://pypi.org/project/pyperclip/)\* & [graeScripts.Drawing](src/graeScript/Drawing) |Returns/copies to the clipboard either the RGB or the Hex color values of a given an HTML color name.|
|**pf_fix_path_sep.py**|[pyperclip](https://pypi.org/project/pyperclip/)|Takes path from clipboard, replaces `\` path separators with `/`, and copies new string to clipboard.|

*\*Code can be altered relatively easily to remove dependency.*

# [`graeScript`](src/graeScript) Details

(*In progress*)

## [`graeScript.htmlcolors`](src/greScript/htmlcolors.py)

A class and a few functions related to [HTML Color Names](https://www.w3schools.com/colors/colors_names.asp) including their color groups, HEX values, and RGB values.

- Requires [Pyperclip](https://pypi.org/project/pyperclip/)

### *class* `HtmlColors`

Return values related to all HTML Color Names.

#### *HtmlColors.*`all` -> list[sqlite4.Row]

Return the color group, name, the RGB and Hex values for every HTML color name.

#### *HtmlColors.*`names` -> list[str]

Return all HTML color names.

## *HtmlColors.*`map_to_name` -> dict[sqlite3.Row]

Map `*HtmlColors.*all` to the HTML color names.

### *HtmlColors.*`map_to_group` -> dict[list[sqlite3.Row]]

Map `*HtmlColors.*all` to the HTML color names.

### `color_value(`*format*: str, *colorname*: str`) -> tuple[str]`

The first item in tuple is the *color* in proper HTML Color Name format, and the second item is either the color's RGB or HEX value depending on *format*.

### `get_colorvalue(`*color*: str, *format*: str, *to_clipboard*: bool = False`) -> None`

- Requires [Pyperclip](https://pypi.org/project/pyperclip/)

Prints *color* in proper HTML Color Name format, and either the color's RGB or HEX value depending on *format*. If *to_clipboard* is `True`, the RGB/HEX value is also copied to the clipboard.

### `get_group_colornames(`*color_group*: str, *to_clipboard*: bool = False`) -> None`

- Requires [Pyperclip](https://pypi.org/project/pyperclip/)

Print or copy to the clipboard all HTML color names in *color_group*.

## [`graeScript.file_explorer.delete_move_dirs`](src/graeScript/file_explorer/delete_move_dirs.py)

### `rename_file(`*source*: Path | str, *destination*: Path, *test*: bool = True`) -> None`

Rename *source* file to *destination* file.

Prints changes made.

If *test* is `True`, no file changes are made.

### `delete_file(`*file*: Path | str, *test*: bool = True`) -> None`

Deletes *file*.

Prints changes made.

If *test* is `True`, no file changes are made.

### `delete_folder(`*dir*: Path | str, *test*: bool = True`) -> None`

Deletes *dir* if it is empty.

Prints changes made.

If *test* is `True`, no file changes are made.

### `delete_empty_tree(`*dir*: Path | str, *test*: bool = True`) -> None`

Deletes empty folders within directory's tree.

Prints changes made

If *test* is `True`, no file changes are made.

### `glob_delete(`*dir*: Path | str, *glob_pattern*: str, *test*: bool = True`) -> None`

Deletes files in directory *dir* based on the glob pattern in *glob_pattern*.

Prints changes made.

If *test* is `True`, no file changes are made.

### `move_contents(`*source*: Path | str, *destination*: Path, *test*: bool = True, *\*args*: str) -> list[dict]

Move all of *source* directory's contents into *destination*. Prints changes made.

If *test* is `True`, no file changes are made.

*\*args* takes either 'replace', 'delete', 'compare', or None which dictates how move conflicts will be handled.

- 'replace': replace file in *destination* with the conflicting one from *source*
- 'delete': delete file in *source*
- 'compare': compares the last edit date of the files in conflict, keeping whichever has the most recent date. (Either moves or deletes *source*)
- If no argument is passed for *\*args*, this function returns details about files that weren't moved and their matching destination file.

### `_walk_and_combine(`*start_dir*: Path | str, *dest_pattern*: str, *match_group_num*: int, *test*: bool = `True`, *\*args*: str`) -> None`

(**Needs testing after previous refactoring into some of above functions**)

Walk through *start_dir* and combine move files into folders in *start_dir* matching destination_pattern's match group number.

Prints changes made.

If *test* is `True`, no file changes are made.

*\*args* takes either 'replace', 'delete', 'compare', or None which dictates how move conflicts will be handled.

- 'replace': replace file in *destination* with the conflicting one from *start_dir*
- 'delete': delete file in *start_dir*
- 'compare': compares the last edit date of the files in conflict, keeping whichever has the most recent date. (Either moves or deletes *start_dir*)
- If no argument is passed for *\*args*, then any conflict files will not be moved.

## [`graeScript.file_explorer.edit_filename`](src/graeScript/file_explorer/edit_filename.py)

### `change_file_ext(`*file*: Path | str, *new_ext*: str, *Test*: bool = `True``) -> None`

Rename *file* by replacing it's existing extension with *new_ext*.

Prints changes made.

If *test* is `True`, no file changes are made.

### `change_file_ext_in(`*dir*: Path | str, *new_ext*: str, *replace_ext*: str = `'*.*'`, *Test*: bool = `True``) -> None`

Rename files in *dir* by replacing their existing extension with *new_ext*.

If *replace_ext* is uses, then only the files with *replace_ext* will be renamed.

Prints changes made.

If *test* is `True`, no file changes are made.

## [`graeScript.file_explorer.find_files`](src/graeScript/file_explorer/find_files.py)

### `search_for(`*dir*: Path | str, *glob*: str`) -> list[Path]:`

Search the directory tree `dir` and returns files matching `glob`.

### `found_files_to_text(`*dir*: Path | str, *glob*: Path | str, *txt_file*: Path | str`) -> list[Path]:`

Call `search_for()` and output found file paths to `txt_file`.

## [`graeScript.file_explorer.find_photo_folder`](src/graeScript/file_explorer/find_photo_folder.py)

- Requires [Pillow](https://pypi.org/project/Pillow/)

### `find_photo_folder(`*start_dir*: str`)`

From [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) by Al Sweigart [Chapter 17](https://automatetheboringstuff.com/chapter17/#calibre_link-3617)

## [`graeScript.markdown.to_md_list`](src/graeScript/markdown/to_md_list.py)

- Requires [Pyperclip](https://pypi.org/project/pyperclip/)

### `bullet_list(`*text*: str, *as_todo*: bool = `False) -> list`

Create a markdown bulleted list from *text*. If *as_todo* is `True`, bullets are written as '- [ ]' instead of '-'.

Determines list items and level by number of spaces of indentation.

### `from_clipboard(`*as_todo*: bool = `False) -> None:)`

- Requires [Pyperclip](https://pypi.org/project/pyperclip/)

Uses `bullet_list`, taking *text* from clipboard.

## [`graeScript.markdown.to_md_table`](src/graeScript/markdown/to_md_table.py)

### `table(`*rows*: list | tuple, *align*: str = 'l', *center_header*: bool = True, *col_padding*: int = 0, *header_row*: list = []`) -> None`

Prints a markdown table our of *rows*.

## [`graeScript.markdown.PDFiles/create_pdfs`](src/graeScript/PDFiles/create_pdfs.py)

- Requires [PyPDF2](https://pypi.org/project/PyPDF2/)

## [`graeScript.markdown.getPDFtext`](src/graeScript/PDFiles/getPDFtext.py)

- Requires [PyMuPDF](https://pypi.org/project/PyMuPDF/)

## [`graeScript.utils.convert_nums`](src/graeScript/utils/convert_nums.py)

Functions related to converting numbers from one base to others.

### `get_decimal(`*digit*: int | str`) -> int`

Convert a decimal, binary, hexadecimal, or octal to an integer.

### `builtin_convert(`*digit*: int | str, *include_prefix*: bool = False, *hex_case*=`str.upper) -> list`

Obtain decimal, hexadecimal, and binary value for an integer decimal.

### `numbers_to_md_table(`*start_num*: int | str, *stop_num*: int | str, *include_prefix*: bool = `False) -> None`

Prints markdown number conversion table from *start_num* through *stop_num*.

## [`graeScript.utils.isleap`](src/graeScript/utils/isleap.py)

Can be used in terminal `py isleap.py <year>` and prints message to inform if *year* is a leap year or not.

### `isleap(`*year*: int`) -> Bool`

Returns `True` if *year* entered is a leap year.

## [`graeScript.utils.mergetxt`](src/graeScript/utils/mergetxt.py)

### `mergetext(`*file1*: str, *file2*: str`) -> set`

Merge two text files in which each line contains one word.

## [`graeScript.utils.validation](src/graeScript/utils/validation.py)

From [Python Documentation: HOWTO Descriptors](https://docs.python.org/3/howto/descriptor.html#validator-class)

### *class* `Validator`

> A validator is a descriptor for managed attribute access. Prior to storing any data, it verifies that the new value meets various type and range restrictions. If those restrictions aren't met, it raises an exception to prevent data corruption at its source. - [PyDocs](https://docs.python.org/3/howto/descriptor.html#validator-class)

### *class* `String(Validator)`

> `String` verifies that a value is a str. Optionally, it validates a given minimum or maximum length. It can validate a user-defined predicate as well. - [PyDocs](https://docs.python.org/3/howto/descriptor.html#custom-validators)

### *class* `Number(Validator)`

> `Number` verifies that a value is either an int or float. Optionally, it verifies that a value is between a given minimum or maximum. - [PyDocs](https://docs.python.org/3/howto/descriptor.html#custom-validators)

### *class* `OneOf(Validator)`

> `OneOf` verifies that a value is one of a restricted set of options." - [PyDocs](https://docs.python.org/3/howto/descriptor.html#custom-validators)
