#! python3
"""In terminal, prints whether year is or isn't a leap year.

To use in terminal: py isleap.py <year>
"""


def isleap(year: int):
    """Returns True if year entered is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print('Usage: python isleap.py [year]')
        sys.exit()

    year = int(sys.argv[1])
    if isleap(year):
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')
