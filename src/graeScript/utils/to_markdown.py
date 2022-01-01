import copy


def _check_arg_for(align: str) -> None:
    """
    Ensure that the argument passed to align is acceptable.

    Args:
        `align` (str):
            The alignment arg passed to another function.

    Raises:
        `SystemExit`: If alignment arg is unacceptable.
    """
    if align not in {'r', 'l', 'c', 'm'}:
        print('Expected align to be "(r)ight", "(l)eft", "(c)enter",'
              f' or "(m)ixed" not "{align}".')
        raise SystemExit


def _align_row(row: list, col_widths: list[int], align: str
               ) -> list[str]:
    """
    Add spacing and alignment to string value of each item in row.

    Args:
        `row` (list):
            The context of a row of items.
        `col_widths` (list[int]):
            The widths for each column of the row. The number of
            items in col_widths must be the same as in row.
        `align` (str):
            How every item in row should be aligned.
            Accepts one (1) of the following:
                'r': right-aligned
                'l': left-aliged
                'c': center-aligned
                'm': mixed; align towards the middle column(s).
                    The left-half of table is right-aligned.
                    The middle 1 or 2 columns are center-aligned.
                    The right-half of the table is left-aligned.
    Returns:
        list[str]: The items of row formatted per col_widths and align.

    Example:
    >>> pets = ['dog', 'cat', 'parrot']
    >>> widths = [5, 5, 8]
    >>> alignments = ('l', 'c', 'r', 'm')
    >>> for alignment in alignments:
    ...     print(_align_row(pets, widths, alignment))
    ['dog  ', 'cat  ', 'parrot  ']
    [' dog ', ' cat ', ' parrot ']
    ['  dog', '  cat', '  parrot']
    ['  dog', ' cat ', 'parrot  ']
    >>> pets = ['dog', 'cat', 'parrot', 'snake']
    >>> widths = [10, 10, 10, 10]
    >>> for alignment in alignments:
    ...     print(_align_row(pets, widths, alignment))
    ['dog       ', 'cat       ', 'parrot    ', 'snake     ']
    ['   dog    ', '   cat    ', '  parrot  ', '  snake   ']
    ['       dog', '       cat', '    parrot', '     snake']
    ['       dog', '   cat    ', '  parrot  ', 'snake     ']
    """
    # Quit the program if the argument passed to align is invalid.
    _check_arg_for(align)
    # Obtain the number of columns in the row.
    num_cols = len(row)
    if num_cols != len(col_widths):
        raise Exception(f'The number of items in rows ({num_cols}) does not'
                        ' match the number of items in col_widths.'
                        f' ({len(col_widths)})')
    # Set the alignment for each item in the row.
    if align == 'r':  # Right-align
        row = [f'{row[i]:>{col_widths[i]}}' for i in range(num_cols)]
    elif align == 'l':  # Left-align
        row = [f'{row[i]:<{col_widths[i]}}' for i in range(num_cols)]
    elif align == 'c':  # Center-align
        row = [f'{row[i]:^{col_widths[i]}}' for i in range(num_cols)]
    else:  # Align toward center column(s).
        # Obtain the location of the middle 1 or 2 columns, and
        # of the left and right halves of the table.
        half = num_cols // 2
        half_remainder = num_cols % 2
        if half_remainder:
            row = [
                f'{row[i]:^{col_widths[i]}}' if i == half else
                f'{row[i]:>{col_widths[i]}}' if i < half else
                f'{row[i]:<{col_widths[i]}}'
                for i in range(num_cols)]
        else:
            end_l = half - 1
            start_r = half + 1
            row = [
                f'{row[i]:^{col_widths[i]}}' if end_l <= i < start_r else
                f'{row[i]:>{col_widths[i]}}' if i < end_l else
                f'{row[i]:<{col_widths[i]}}'
                for i in range(num_cols)]
    return row


def table(rows: list | tuple, align: str = 'l', center_header: bool = True,
          col_padding: int = 0, header_row: list = []) -> None:
    """
    Print a markdown table containing the data in rows.

    Args:
        `rows` (list | tuple):
            A 2-dimension list or tuple containing the content for each
            row and column of the output table.  The first item should be
            row headers otherwise, pass the header row to `header_row`.
        `align` (str, Optional): Defaults to 'l'.
            The text aligned within the table's rows and columns.
            Accepts one (1) of the following:
                'r': right-aligned
                'l': left-aliged
                'c': center-aligned
                'm': mixed/aligned toward middle column(s)
        `center_header` (bool, opt): Defaults to True.
            Whether to center-align header.
                If False, header row is aligned per `align`.
                If True, header row is always center-aligned.
        `col_padding` (int, Optional): Defaults to 0.
            The amount of spacing to add between the column delimiters
            and the contents of each column text.
        `header_row` (list, Optional): Defaults to [].
            The values to be used as column headers for the table.
            Should be used if `rows` does not already contain a header row.

    >>> table([['cat', 'dog'], ['parrot', 'snake']],
    ...       'l', True, 1, ['pet1', 'pet2'])
    |  pet1  | pet2  |
    |--------|-------|
    | cat    | dog   |
    | parrot | snake |
    >>> table([['Jeff', 'dog', 'Marlow'], ['Plush', 'cat', 'Sassy'],
    ...         ['Prince', 'bird', 'Fern'], ['Severus', 'snake', 'Slim']],
    ...       'm', True, 1, ['Your Pet Name', 'Pet Type', 'My Pet Name'])
    | Your Pet Name | Pet Type | My Pet Name |
    |---------------|----------|-------------|
    |          Jeff |   dog    | Marlow      |
    |         Plush |   cat    | Sassy       |
    |        Prince |   bird   | Fern        |
    |       Severus |  snake   | Slim        |
    >>> table([['Jeff', 'dog', 'mammal', 'Marlow'],
    ...        ['Plush', 'cat', 'mammal',  'Sassy'],
    ...        ['Prince', 'parrot', 'bird', 'Fern'],
    ...        ['Severus', 'snake', 'reptile', 'Slim']],
    ...       'm', True, 1,
    ...       ['Your Pet Name', 'Pet Type', 'Category', 'My Pet Name'])
    | Your Pet Name | Pet Type | Category | My Pet Name |
    |---------------|----------|----------|-------------|
    |          Jeff |   dog    |  mammal  | Marlow      |
    |         Plush |   cat    |  mammal  | Sassy       |
    |        Prince |  parrot  |   bird   | Fern        |
    |       Severus |  snake   | reptile  | Slim        |
    """
    # Quit the program if the argument passed to align is invalid.
    _check_arg_for(align)
    # Copy rows list passed to function or convert rows to a list.
    if isinstance(rows, list):
        rows: list = copy.deepcopy(rows)
    else:
        rows: list = list(rows)
    # Insert header row if one was passed.
    if header_row:
        rows.insert(0, header_row)

    # Obtain the number of columns in the table.
    num_cols: int = len(rows[0])
    # For every column, set the width based on it's longest item.
    col_widths: list[int] = [max([len(str(i[j])) for i in rows[:]])
                             for j in range(num_cols)]
    # Insert a row of hypens for markdown table header marker.
    rows.insert(1, ['-' * col_widths[i] for i in range(num_cols)])

    # Print out the markdown table row by row.
    for row_num, row in enumerate(rows):
        # Set the padding for the row.
        pad = ' ' * col_padding
        if row_num == 1:
            # Print out the markdown header marker.
            pad = '-' * col_padding
        # Add text alignment to the row items
        if row_num == 0 and center_header:
            # Center-align header.
            row = _align_row(row, col_widths, 'c')
        else:
            # Align remaining rows and/or align header
            # row the same as the rest of the table.
            row = _align_row(row, col_widths, align)
        # Print the row
        for col in row:
            print('|', col, sep=pad, end=pad)
        # Print row's last vertical bar.
        print('|')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
