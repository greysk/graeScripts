#! python3
"""Transforms text to a markdown bulleted list based on indentation.

Contains:
    `bullet_list(text: str) -> list[str]`
        : Converts the text passed to it into a markdown list.
        : Each item in list is a line of the text ending in a newline.

    `from_clipboard() -> None`
        : Takes text from clipboard and transforms it into a markdown list.
        : Places transformed text into clipboard.
        - Can be run as a module in another file or as a script in a CLI.
        - Dependency: pyperclip module.
"""
import re
import io


def bullet_list(text: str) -> list:
    r"""
    Converts the text passed to it into a markdown list based on indentation.

    Args:
        `text` (str): The text containing test to be made into a markdown list.

    Returns:
        list: Contains each line of the text. Each item ends with `"\n"`
    """
    lines = text.splitlines()
    # Define one indent as being two spaces to match Markdown indent.
    one_indent = r'\s{2}'
    pattern = re.compile(one_indent)
    # Obtain number of indents in the line with the least number of indents.
    min_num_indents = min([len(pattern.findall(line)) for line in lines
                           if pattern.match(line)])
    # Adjust pattern to find lines of list items based on min_num_indents.
    pattern = re.compile(
        rf'''
        ^({one_indent}){{{min_num_indents}}}  # == (' ' * 2) * min_num_indents
        ([ ]*\w)  # Captured to adjust for nested list items.
        ''',
        re.VERBOSE)
    # Add markdown-style list bullets to lines matching intent rule.
    for i, line in enumerate(lines):
        # Replacing leading min_num_indents with "- "
        newline = pattern.sub(r'- \2', line, 1)
        # Adjust for nested list items.
        match = re.match(r'^[-]((\s){2,}) \w', newline)
        if match:
            min_num_indents = len(match.group(1)) // min_num_indents
            # Remove excess space after '-' and appropriate nest list items.
            newline = newline.replace(match.group(1), '').replace(
                '-', f'{"  " * min_num_indents}-')
        # Replace line in lines with newline
        lines[i] = f'{newline}\n'
    return lines


def from_clipboard() -> None:
    """
    Uses bullet_list() with clipboard. Uses pyperclip.

    Passes copied text to bullet_list(), makes returned value into text,
    and copies transformed text to the clipboard.
    """
    # No reason to include pyperclip in the namespace of the entire file.
    import pyperclip
    # Get text from the clipboard.
    last_copied = pyperclip.paste()
    # Write text into a memory buffer to get proper output format.
    membuffer = io.StringIO()
    membuffer.writelines(bullet_list(last_copied))
    # Read text from memory buffer into clipboard.
    pyperclip.copy(membuffer.getvalue())
    membuffer.close()


if __name__ == '__main__':
    from_clipboard()
