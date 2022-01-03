import pytest

from graeScript.utils.convert_nums import (get_decimal)


class TestGetDigit:
    def test_from_bi(self):
        bis = [('0b10', 2), ('0b1000', 8), ('0b10101011', 171),
               ('0b1111011', 123), ('0b1000', 8), ('0b0', 0), ('0b0', 0)]
        for i, o in bis:
            assert get_decimal(i) == o

    def test_from_oct(self):
        octs = [('0o12', 10), ('0o14', 12), ('0o6', 6), ('0o0', 0),
                ('0o42', 34), ('0o745', 485), ('0o34', 28), ('0o20', 16),
                ('0o1', 1)]
        for i, o in octs:
            assert get_decimal(i) == o

    def test_from_dec(self):
        decimals = [(12, 12), (14, 14), (6, 6), (0, 0), ('42', 42),
                    ('745', 745), ('34', 34), ('20', 20), ('1', 1)]
        for i, o in decimals:
            assert get_decimal(i) == o

    def test_from_hex(self):
        hexes = [('0xA', 10), ('0xF', 15), ('0x3', 3), ('0x0', 0),
                 ('0xFFFF', 65535), ('0x431', 1073), ('0x50', 80),
                 ('0x210D', 8461), ('0x1979', 6521), ('0x7F0', 2032)]
        for i, o in hexes:
            assert get_decimal(i) == o

    def test_wrong_type(self):
        wrong_type = [3.45, (1, 2, 3), {'cat': 5, 7: '14'}]
        with pytest.raises(TypeError):
            for i in wrong_type:
                assert get_decimal(i)

    def test_wrong_key(self):
        wrong_key = ['parrot', '0i35', '0110110', '3.145']
        with pytest.raises(KeyError):
            for i in wrong_key:
                assert get_decimal(i)
