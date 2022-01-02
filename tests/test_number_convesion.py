from random import randint

from graeScript.utils.convert_nums import (get_decimal,
                                           builtin_convert,
                                           numbers_to_md_table)

class TestHexadecimal:
    def test_hexdigit_to_decimal(self):
        hex_decimal = [('A', 10), ('F', 15), ('3', 3), ('0', 0)]
        for h, d in hex_decimal:
            assert digit_to_hex_decimal(h) == d

    def test_hexdigit_to_binary(self):
        hex_binary = [('A', '1010'), ('F', '1111'), ('3', '11'), ('0', '0')]
        for h, b in hex_binary:
            assert digit_to_hex_binary(h) == b

    def test_hex_to_binary(self):
        hex_binary = [(['87', False], '10000111'), (['A5', False], '10100101'),
                      (['0x141', False], '101000001'), (['0x5', False], '101'),
                      (['0x10', True], '0b10000'), (['0x4', True], '0b100'),
                      (['401', True], '0b10000000001'), (['7', True], '0b111'),
                      (['0', False], '0'), (['0x0', False], '0'),
                      (['0', True], '0b0'), (['0x0', True], '0b0')
                      ]
        for h, b in hex_binary:
            assert hexadecimal_to_binary(h[0], h[1]) == b

    def test_hex_to_decimal(self):
        hex_decimal = [('FFFF', 65535), ('431', 1073), ('210D', 8461),
                       ('0x1979', 6521), ('0x50', 80), ('0x7F0', 2032),
                       ('0', 0), ('0x0', 0)]
        for h, d in hex_decimal:
            assert hexadecimal_to_decimal(h) == d


class TestDecimal:
    def test_decimaldigit_to_hex(self):
        decimal_hex = [(12, 'C'), (14, 'E'), (6, '6'),
                       (0, '0')]
        for d, h in decimal_hex:
            assert digit_to_hex_decimal(d) == h

    def test_decimal_to_binary(self):
        dec_binary = [([1, False], '1'), ([11, False], '1011'),
                      ([2, True], '0b10'), ([123, True], '0b1111011'),
                      ([0, False], '0'), ([0, True], '0b0')]
        for d, b in dec_binary:
            assert decimal_to_binary(d[0], d[1]) == b

    def test_decimal_to_hex(self):
        dec_hex = [([100, False], '64'), ([2120, False], '848'),
                   ([869464, False], 'D4458'), ([16859, True], '0x41DB'),
                   ([34, True], '0x22'), ([156191, True], '0x2621F'),
                   ([0, False], '0'), ([0, True], '0x0')]
        for d, h in dec_hex:
            assert decimal_to_hexadecimal(d[0], d[1]) == h


class TestBinary:
    def test_binarydigit_to_hex(self):
        binary_hex = [(1100, 'C'), (1110, 'E'), (110, '6'),
                      (0, '0')]
        for b, h in binary_hex:
            assert digit_to_hex_binary(b) == h

    def test_binary_to_decimal(self):
        binary_dec = [(10, 2), (1000, 8), (10101011, 171),
                      ('0b1111011', 123), ('0b1000', 8),
                      (0, 0), ('0b0', 0)]
        for b, d in binary_dec:
            assert binary_to_decimal(b) == d

    def test_binary_to_hex(self):
        binary_hex = [([10110001, False], 'B1'), ([1110101, False], '75'),
                      (['0b10101', False], '15'), (['0b1101110', False], '6E'),
                      (['0b100001', True], '0x21'), (['0b1110', True], '0xE'),
                      ([0, False], '0'), (['0b0', False], '0'),
                      ([0, True], '0x0'), (['0b0', True], '0x0')]
        for b, h in binary_hex:
            assert binary_to_hexadecimal(b[0], b[1]) == h


class TestAll:
    conversion_table = [
            [0, '0x0', '0b0'],
            [1, '0x1', '0b1'],
            [2, '0x2', '0b10'],
            [3, '0x3', '0b11'],
            [4, '0x4', '0b100'],
            [5, '0x5', '0b101'],
            [6, '0x6', '0b110'],
            [7, '0x7', '0b111'],
            [8, '0x8', '0b1000'],
            [9, '0x9', '0b1001'],
            [10, '0xA', '0b1010'],
            [11, '0xB', '0b1011'],
            [12, '0xC', '0b1100'],
            [13, '0xD', '0b1101'],
            [14, '0xE', '0b1110'],
            [15, '0xF', '0b1111'],
            ]

    def builtin_convert(self, digit):
        output = []
        if isinstance(digit, int):
            output.append(digit)
            hex_digit = hex(digit)[:2] + hex(digit)[2:].upper()
            output.append(hex_digit)
            output.append(bin(digit))
        return output

    def test_digit_to(self):
        assert (digit_to_hex_binary('F')
                == self.conversion_table[digit_to_hex_decimal('F')][2][2:])

    def test_to_all1(self):
        for i in self.conversion_table:
            for n in i:
                assert to_all(n, True) == i

    def test_to_all2(self):
        digit = randint(1, 10000)
        assert to_all(digit, True) == self.builtin_convert(digit)
