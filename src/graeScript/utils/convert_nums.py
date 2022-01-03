"""Functions related to converting numbers from one base to others.

get_decimal(digit: int | str) -> int
    : Convert a decimal, binary, hexadecimal, or octal to an integer.

builtin_convert(digit: int, include_prefix: bool = True,
                hex_case=str.upper) -> list
    : Obtain decimal, hexadecimal, and binary value for an integer decimal.

numbers_to_md_table(start_num: int, stop_num: int,
                    include_prefix: bool = False) -> None
    : Prints a markdown table containing the decimal, hexadecimal, and
      binary values for the numbers from start_num to stop_num
"""
from graeScript.markdown import to_md_table


def get_decimal(digit: int | str) -> int:
    """
    Convert a decimal, binary, hexadecimal, or octal to an integer.

    Args:
        digit (int | str): The digit to be converted. Non-decimal
        numbers must begin with their associated prefix (binary = '0b',
        hexadecimal = '0x', octal = '0o').
    Raises:
        TypeError: If digit is neither an integer or str.

    Returns:
        int: digit's integer decimal value.
    """
    if isinstance(digit, int) or (isinstance(digit, str)
                                  and digit.isdecimal()):
        return int(digit)
    if not isinstance(digit, str):
        raise TypeError()
    bases = {'0x': 16, '0b': 2, '0o': 8}
    decimal = int(digit, bases[digit[:2]])
    return decimal


def builtin_convert(digit: int | str, include_prefix: bool = False,
                    hex_case=str.upper) -> list:
    """
    Obtain decimal, hexadecimal, and binary value for an integer decimal.

    Args:
        `digit` (int):
            The integer decimal to be converted.
        `include_prefix` (bool, opt): Defaults to False.
            If True, the output hexadecimal number starts with '0x',
            the output binary number starts with '0b', and the output
            octal number starts with '0o'

    Raises:
        `TypeError`: If a non-interger is passed to digit.

    Returns:
        list: The digit, hexadecimal, and binary number.

    Example:
    >>> test_values = (4, '0xFF', '0b01101', '0o35')
    >>> for value in test_values:
    ...     builtin_convert(value)
    [4, '100', '4', '4']
    [255, '11111111', '377', 'FF']
    [13, '1101', '15', 'D']
    [29, '11101', '35', '1D']
    """
    converted_digits: list = []
    # Convert input digit to an integer decimal and add to output list.
    digit = get_decimal(digit)
    converted_digits.append(digit)
    # Convert integer decimal to binary and octal.
    binum: str = bin(digit)
    octal: str = oct(digit)
    # Convert integer to hexadecimal and make everything after '0x'
    # match the case denoted by hex_case.
    hexnum: str = hex_case(hex(digit)[2:])
    # Adjust output for include_prefix argument.
    if include_prefix:
        converted_digits.append(binum)
        converted_digits.append(octal)
        converted_digits.append(hex(digit)[:2] + hexnum)
    else:
        converted_digits.append(binum[2:])
        converted_digits.append(octal[2:])
        converted_digits.append(hexnum)
    return converted_digits


def numbers_to_md_table(start_num: int | str,
                        stop_num: int | str,
                        include_prefix: bool = False) -> None:
    """
    Prints markdown number conversion table from start_num through stop_num.

    Args:
        start_num (int | str):
            Start number in decimal, binary, octal, or hex. Inclusive.
            Non-decimal numbers must be prefixed with 0b, 0o, or 0x.
     (int | str):
            Stop number in decimal, binary, octal, or hex. Inclusive.
            Non-decimal numbers must be prefixed with 0b, 0o, or 0x.
        include_prefix (bool, opt):
            Defaults to False. If True, hex number starts with 0x and
            binary number starts with 0b.

    Example:
    >>> numbers_to_md_table(0, 5, True)
    | Decimal | Binary | Octal | Hex |
    |---------|--------|-------|-----|
    |       0 |    0b0 |   0o0 | 0x0 |
    |       1 |    0b1 |   0o1 | 0x1 |
    |       2 |   0b10 |   0o2 | 0x2 |
    |       3 |   0b11 |   0o3 | 0x3 |
    |       4 |  0b100 |   0o4 | 0x4 |
    |       5 |  0b101 |   0o5 | 0x5 |
    """
    ROW_HEADERS = ['Decimal', 'Binary', 'Octal', 'Hex']
    # Create a list containing lists of the decimal, binary, octal, and
    # hexadecimal value of each number from start_num through stop_num.
    rows = [builtin_convert(i, include_prefix)
            for i in range(start_num, stop_num + 1)]
    # Print out markdown table of the converted numbers lists in rows.
    to_md_table.table(rows, align='r', center_header=True,
                      col_padding=1, header_row=ROW_HEADERS)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
