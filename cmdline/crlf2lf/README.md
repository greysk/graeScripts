# CRLF_to_LF ReadMe

```txt
py -m CRLF_to_LF.py -h
usage: CRLF_to_LF.py [-h] [-t] [-v] folder [folder ...]

Change files in the tree of the path provided to have LF newline endings. When run without
any optional flags, the files are replaced in-place i.e., The original files are overwritten.

positional arguments:
  folder         The path to the top folder of the tree.

options:
  -h, --help     show this help message and exit
  -t, --test     Run in test mode. If test mode but not verbose, asks for output file
                 and converted files are sent to that folder.
                 If verbose flag is used with test, no files are created.
  -v, --verbose  Run in verbose mode. Prints each file path of the file being changed
```
