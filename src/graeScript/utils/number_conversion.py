"""
Functions that convert numbers between decimal, hexadecimal, and binary.

Contains:
    digit_to_hex_decimal()
      : Convert a str hexadecimal digit to an int decimal digit or vice versa.
    digit_to_hex_binary()
      : Convert a str hexadecimal digit to an int binary digit or vice versa.
    binary_to_decimal()
      : Convert a binary number (str | int) to a decimal number (int).
    decimal_to_binary()
      : Convert a decimal number (str) to a binary number (str).
    hexadecimal_to_decimal()
      : Convert a hexadecimal number (str) to a decimal number (int).
    decimal_to_hexadecimal()
      : Convert a decimal number (int) to a hexadecimal number (str).
    hexadecimal_to_binary()
      : Convert a hexadecimal number (str) to a binary number (str).
    binary_to_hexadecimal()
      : Convert a binary number (int | str) to a hexadecimal number (str).
    to_all()
      : Convert input number into list containing decimal, hexadecimal, binary.
    builtin_convert()
      : Coverts decimal number into list containing decimal, hexadecimal,
        binary using hex() and bin() built-in function.
"""
from graeScript import to_markdown_table

DIGIT_HEX2DECIMAL = {'0': 0, '1': 1, '2': 2, '3': 3,
                     '4': 4, '5': 5, '6': 6, '7': 7,
                     '8': 8, '9': 9, 'A': 10,  'B': 11,
                     'C': 12, 'D': 13, 'E': 14, 'F': 15
                     }

DIGIT_DECIMAL2HEX = {0: '0', 1: '1', 2: '2', 3: '3',
                     4: '4', 5: '5', 6: '6', 7: '7',
                     8: '8', 9: '9', 10: 'A', 11: 'B',
                     12: 'C', 13: 'D', 14: 'E', 15: 'F'
                     }

DIGIT_HEX2BINARY = {'0': '0', '1': '1', '2': '10', '3': '11',
                    '4': '100', '5': '101', '6': '110', '7': '111',
                    '8': '1000', '9': '1001', 'A': '1010',  'B': '1011',
                    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
                    }

DIGIT_BINARY2HEX = {'0': '0', '1': '1', '10': '2', '11': '3',
                    '100': '4', '101': '5', '110': '6', '111': '7',
                    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}


def digit_to_hex_decimal(digit: str | int) -> int | str:
    """
    Convert 1 hexadecimal digit to its decimal equivalent or vice versa.

    Primary purpose is to convert between the alphabetical hexadecimal digits.

    Args:
        digit (str | int): Hexadecimal digit must be str. Decimal must be int.

    Returns:
        int | str:
            int: The decimal version of input hexadecimal string.
            str: The string version of input decimal integer.

    Examples:
    >>> print(digit_to_hex_decimal('A'))
    10
    >>> print(digit_to_hex_decimal(10))
    'A'
    >>> print(digit_to_hex_decimal('F'))
    15
    >>> print(digit_to_hex_decimal(15))
    'F'
    """
    # Define hex to int dictionary.
    if isinstance(digit, int):
        # Make an int to hex dictionary by swapping keys and values.
        conversion_dict = DIGIT_DECIMAL2HEX
    else:
        conversion_dict = DIGIT_HEX2DECIMAL
    return conversion_dict.get(digit)


def digit_to_hex_binary(digit: int | str) -> str | int:
    """
    Converts 1 hexadecimal digit to its binary equivalent or vice versa.

    Primary purpose is to convert between the alphabetical hexadecimal digits.

    Args:
        digit (str | int): Hexadecimal digit must be str. Binary must be int.

    Returns:
        int | str:
            int: The binary version of input hexadecimal string.
            str: The hexadecimal version of input binary integer.

    Examples:
    >>> print(digit_to_hex_binary('A'))
    1010
    >>> print(digit_to_hex_binary(1010))
    'A'
    >>> print(digit_to_hex_binary('F'))
    1111
    >>> print(digit_to_hex_binary(1111))
    'F'
    """
    if isinstance(digit, int):
        # Make a binary to hex dictionary, but swapping keys and values.
        conversion_dict = DIGIT_BINARY2HEX
    else:
        conversion_dict = DIGIT_HEX2BINARY
    return conversion_dict.get(str(digit))


def hexadecimal_to_decimal(hex_num: str) -> int:
    """Convert a hexadecimal number to a decimal integer.

    Args:
        hex_num: The hexadecimal number to be converted.

    Returns:
        int: The decimal integer representing hex_num.

    Examples:

    >>> print(hexadecimal_to_digit('FFFF'))
    65535
    >>> print(hexadecimal_to_digit('431'))
    1073
    >>> print(hexadecimal_to_digit('0x431'))
    1073
    """
    hex_num = str(hex_num)
    if hex_num.startswith('0x'):
        hex_num = hex_num[2:]
    n = len(hex_num)
    decimal = 0
    for d in hex_num:
        d = digit_to_hex_decimal(d)
        n -= 1
        step_result = d * (16 ** n)
        decimal += step_result
    return decimal


def hexadecimal_to_binary(hex_num: str, binary_prefix: bool = False) -> str:
    """
    Convert a hexadecimal number to a binary number.

    Args:
        hex_num (str): The hexadecimal number to be converted to binary.

    Returns:
        str: The binary number representing the hex_num.
    """
    # Handle prefixes
    binary = []
    if hex_num.startswith('0x'):
        hex_num = hex_num[2:]
    decimal = hexadecimal_to_decimal(hex_num)
    binary = decimal_to_binary(decimal, binary_prefix)
    return binary


def binary_to_decimal(bi_num: str | int) -> int:
    """Convert a binary number to a decimal number.

    Args:
        bi_num: The binary number to be converted.

    Returns:
        int: The decimal number representing bi_num.
    """
    bi_num = str(bi_num)
    if bi_num.startswith('0b'):
        bi_num = bi_num[2:]
    n = len(bi_num)
    decimal = 0
    for d in bi_num:
        d = int(d)
        n -= 1
        step_result = d * (2 ** n)
        decimal += step_result
    return decimal


def binary_to_hexadecimal(bi_num: int | str,  hex_prefix: bool = False) -> str:
    """
    Covert a binary number to a hexadecimal number.

    Args:
        bi_num (int): The binary number to be converted to hexadecimal
        hex_prefix (bool, optional): Whether to add the hex prefix (0x).
            Defaults to False.

    Returns:
        str: The hexadecimal number representing bi_num
    """
    bi_num = str(bi_num)
    if bi_num.startswith('0b'):
        bi_num = bi_num[2:]
    bi_len = len(bi_num)
    hexadecimal = []
    # Starting from the end, convert every 4 binary numbers to a hex digit.
    step = -4  # To step backwards by 4.
    range_stop = -(bi_len + 1)  # To include final group of 4.
    outside_step = bi_len % abs(step)  # To get and remaining numbers.
    # For loop to slice bi_num from the end in groups of 4.
    for i in range(step, range_stop, step):
        if i == -4:  # bi_num[-4:]
            hex_digit = digit_to_hex_binary(int(bi_num[i:]))
            hexadecimal.append(hex_digit)
        else:  # Remaining groups of 4 from end.
            hex_digit = digit_to_hex_binary(int(bi_num[i:i+4]))
            hexadecimal.append(hex_digit)
    # Convert remaining leading digits.
    if outside_step:
        hex_digit = digit_to_hex_binary(int(bi_num[:outside_step]))
        hexadecimal.append(hex_digit)
    # Put digits in proper order as they are currently backwards.
    hexadecimal.reverse()
    if hex_prefix:
        hexadecimal.insert(0, '0x')
    return ''.join(hexadecimal)


def decimal_to_binary(dec_num: int, binary_prefix: bool = False) -> str:
    """Convert a decimal number to a binary number

    Args:
        dec_num (int): The decimal integer number to be converted.
        binary_prefix (bool, optional): Whether to prefix output with '0b'.
            Defaults to False.

    Returns:
        str: The binary number representing dec_num.

    """
    binary = []
    quotient = dec_num
    while quotient > 0:
        binary.append(str(quotient % 2))
        quotient = quotient // 2
    if not binary and dec_num == 0:
        binary.append('0')
    binary.reverse()
    if binary_prefix:
        binary.insert(0, '0b')
    return ''.join(binary)


def decimal_to_hexadecimal(dec_num: int, hex_prefix: bool = False) -> str:
    """Convert a decimal number to a hexadecimal number.

    Uses hex_digit_value().

    Args:
        dec_num: The decimal number to be converted.
        hex_prefix (optional): Whether to prefix output hex number with '0x'
            Defaults to False.

    Examples:

    >>> print(decimal_to_hexadecimal(123))
    '7B'
    >>> print(decimal_to_hexadecimal(123, True))
    '0x7B'
    >>> print(decimal_to_hexadecimal(1073))
    '431'
    >>> print(decimal_to_hexadecimal(1073, True))
    '0x431'
    """
    hexadecimal = []
    quotient = dec_num
    while quotient > 0:
        # Get modulo, convert int to hex digit str 1-9 or A-F.
        hex_digit = digit_to_hex_decimal(quotient % 16)
        hexadecimal.append(hex_digit)
        quotient = (quotient // 16)
    # Put digits in proper order and join.
    if not hexadecimal and dec_num == 0:
        hexadecimal.append('0')
    hexadecimal.reverse()
    if hex_prefix:
        hexadecimal.insert(0, '0x')
    return ''.join(hexadecimal)


def to_all(digit: int | str, prefix: bool = False) -> list[int, str, str]:
    """
    Returns decimal, hexadecimal, and binary number for given digit.

    Args:
        digit (int | str): The digit to be converted.
            Decimals must be integers.
            Hexadecimals must start with the prefix '0x'.
            Binary numbers but start with the prefix '0b'

    Returns:
        list[int, str, str]: Containing decimal, hexadecimal,
        and 'binary.
    """
    output = []
    if isinstance(digit, int):
        output.append(digit)
        output.append(decimal_to_hexadecimal(digit, prefix))
        output.append(decimal_to_binary(digit, prefix))
        return output
    if digit.startswith('0x'):
        output.append(hexadecimal_to_decimal(digit))
        output.append(digit)
        output.append(hexadecimal_to_binary(digit, prefix))
        return output
    if digit.startswith('0b'):
        output.append(binary_to_decimal(digit))
        output.append(binary_to_hexadecimal(digit, prefix))
        output.append(digit)
        return output
    print(f'{digit} must be integer or start with "0x" or "0b"')
    return None


def builtin_convert(digit):
    output = []
    if isinstance(digit, int):
        output.append(digit)
        hex_digit = hex(digit)[:2] + hex(digit)[2:].upper()
        output.append(hex_digit)
        output.append(bin(digit))
    return output


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

    to_markdown_table(rows, 'm', True, 1, ROW_HEADERS)
