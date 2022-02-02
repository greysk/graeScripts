#! python3
r"""
Converts path separators in most recent clipboard text from \\ to /.

Requires pyperclip (`pip install pyperclip`) by Al Sweigart
    https://pypi.org/project/pyperclip/

In otherwords, changes a copied path from Windows format to Unix/MacOS format.
Useful for coding since in many languages, backslashes in strings are handled
as escape characters.

To use:
1. In a folder that is on the system's path (environmental variable),
   establish a .bat file named 'pfix.bat' or whatever you'd like.
2. Inside of the file, write:
        @py.exe path\to\pf_fix_path_sep.pyw
3. Save and close the file.
4. Press Win+R to run the "run" app, type 'pfix' in the run dialog,
   and press enter or click okay.
5. Paste the now-converted text wherever you'd like to use it.

Alternately, you can run the script by running the python file directly with
`py \path\to\pf_fix_path_sep.pyw` or depending on your set up, by
double-clicking on the file.
"""
import pyperclip

# Get text from clipboard and replace '\\' with '/'.
path = pyperclip.paste().replace('\\', '/')
# Place coverted text in clipboard.
pyperclip.copy(path)
