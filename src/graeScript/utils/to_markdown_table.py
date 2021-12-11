from typing import Iterable
from graeScript.utils.number_conversion import to_all


def align_row(row: list, line_sizes: list[int], align: str
              ) -> list[str]:
    """
    Make each item in row into a string aligned per align.

    Args:
        row (list): [description]
        line_sizes (list[int]): [description]
        align (str): [description]

    Raises:
        SystemExit: [description]

    Returns:
        list[str]: [description]
    """
    if align == 'r':
        row = [f'{row[i]:>{line_sizes[i]}}' for i in range(len(row))]
    elif align == 'l':
        row = [f'{row[i]:<{line_sizes[i]}}' for i in range(len(row))]
    elif align == 'c':
        row = [f'{row[i]:^{line_sizes[i]}}' for i in range(len(row))]
    elif align == 'm':
        num_cols = len(line_sizes)
        # Determine index of middle column(s)
        end_left = num_cols // 2 - 1
        start_right = end_left + 1
        if not num_cols % 2 == 0:
            start_right += 1
        # Align left-half right, middle col(s) center, right-half left.
        row = [f'{row[i]:>{line_sizes[i]}}' if i <= end_left else
               f'{row[i]:<{line_sizes[i]}}' if i >= start_right else
               f'{row[i]:^{line_sizes[i]}}'
               for i in range(num_cols)]
    else:
        print('Align must be one of "r", "l", "c", or "m".')
        raise SystemExit
    return row


def print_md_table(iterable: Iterable, header_row: list = [],
                   alignment: str = 'r', col_padding: int = 0,
                   center_header: bool = True) -> None:
    """
    Print out a markdown-format table of iterable's data.

    Args:
        `iterable` (iterable):
            A 2-dimension iterable of rows and columns.  The first item of the
            argument should contain row headers unless `header_row` is used.
        `header_row` (list, Optional): Defaults to [].
            A list containing column headers to prepend to `iterable`.
        `alignment` (str, opt): Defaults to 'r'.
            How text is aligned within the table's rows and columns.
            Accepts one (1) of the following:
                'r': right-aligned
                'l': left-aliged
                'c': center-aligned
                'm': mixed/aligned toward middle column(s)
        `col_padding` (int, opt): Defaults to 0.
            The amount of spacing to add between column delimiter and the text.
        `center_header` (bool, opt): Defaults to True.
            Whether to center-align header.
                If False, header row is aligned per `alignment`.
                If True, header row is always center-aligned.
    """
    # Quit the program if the argument passed to alignment is invalid.
    if alignment not in {'r', 'l', 'c', 'm'}:
        print('Alignment must be one of'
              ' "(r)ight", "(l)eft", "(c)entered", or "(m)ixed".')
        raise SystemExit

    iterable = list(iterable)
    if header_row:
        iterable.insert(0, header_row)

    num_cols = len(iterable[0])
    col_widths = [max([len(str(i[j])) for i in iterable[:]])
                  for j in range(num_cols)]
    iterable.insert(1, ['-' * col_widths[i] for i in range(num_cols)])

    for row_num, row in enumerate(iterable):
        pad = ' ' * col_padding
        if row_num == 1:
            pad = '-' * col_padding
        # Add text alignment to row items
        if row_num == 0 and center_header:
            row = align_row(row, col_widths, 'c')
        else:
            row = align_row(row, col_widths, alignment)
        # Print the row
        for col in row:
            print('|', col, sep=pad, end=pad)
        print('|')


def numbers_to_md_table(start_num: int | str,
                        stop_num: int | str,
                        include_prefix: bool = False) -> None:
    """
    Print a markdown table of numbers in decimal, hexadecimal, and binary.

    range_start and range_stop must be in the same number format.  If the
    number format passed to it is binary or hexadecimal, the number must be
    a string with the appropriate prefix for the number format.  E.g.,
    '0x' for hexadecimal and '0b' for binary.

    Args:
        range_start (int | str):
            Start row number in decimal, hex, or binary.
        range_stop (int | str):
            Stop row number in decimal, hex, or binary.
        include_prefix (bool, opt): Defaults to False.
            If True, hex and binary prefixes in table.
    """
    ROW_HEADERS = ['Decimal', 'Hex', 'Binary']

    # Create and add the rows of numbers to rows.
    rows = [to_all(i, include_prefix) for i in range(start_num, stop_num)]

    print_md_table(rows, ROW_HEADERS, 'm', 1)


if __name__ == "__main__":
    numbers_to_md_table(50, 90)
