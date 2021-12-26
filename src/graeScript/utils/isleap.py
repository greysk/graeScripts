#! python3
"""Returns True if year entered is a leap year.

To use in terminal: py isleap.py <year>
"""


def isleap(year: int):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print('Usage: python isleap.py [year]')
        sys.exit()
    isleap(sys.argv[1])
