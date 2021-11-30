"""Returns the length of a string entered."""

import sys

if len(sys.argv) < 2:
    print('Usage: python stringlen.py [string_to_check]')
    sys.exit()

to_str_list = [str(i) for i in sys.argv[1:]]

string_to_check = ' '.join(to_str_list)

print(f'There are {len(string_to_check)} characters in:')
print(string_to_check)
print()
