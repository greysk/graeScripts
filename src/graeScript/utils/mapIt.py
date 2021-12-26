#! python3
"""Opens a map in the browser using an address from the CLI or clipboard."""
import pyperclip
import webbrowser


def mapit(address):
    webbrowser.open('https://www.google.com/maps/place/' + address)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        # Get address from command line.
        address = ' '.join(sys.argv[1:])
    else:
        # Get address from clipboard.
        address = pyperclip.paste()
    mapit(address)
