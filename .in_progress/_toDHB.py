#! python3
"""Convert decimal to list containing decimal, hexadecimal, binary numbers"""
import sys


def builtin_convert(digit: int) -> list:
    output = []
    if isinstance(digit, int):
        output.append(digit)
        hex_digit = hex(digit)[:2] + hex(digit)[2:].upper()
        output.append(hex_digit)
        output.append(bin(digit))
    return output


print(builtin_convert(int(sys.argv[1])))
