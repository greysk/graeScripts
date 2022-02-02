# graeScript

This is a package containing various programs written for my own personal use and for learning purposed.

**WARNING**: This is very much a work in progress. There are no guarantees of reliability. In fact, I guarantee that I will make changes to the code within this that will utterly change how anything and everything within here could be used, and I do so frequently. If you would like to use code within here, feel free to do so, but I would highly recommend forking this repo and being very careful about pulling any changes from here into your fork.

Currently this repository contains two, separate groups of code:

1. A couple of small, independent scripts written to be run using Windows run application using batch files. (Found in the [cmdline folder](cmdline).)
2. A Python package called `graeScript` which contains a mess of small, mostly unrelated scripts that I've written. It's primary purpoase was making reuse of these scripts easier for myself and to create a central location for them.

## Details of small, independent scripts in [cmdline](cmdline) dir

|Filename     |Dependencies|Summary|
|-------------|------------|-------|
|**colorvalue.py**|[pyperclip](https://pypi.org/project/pyperclip/)\* & [graeScripts.Drawing](src/graeScript/Drawing) |Returns/copies to the clipboard either the RGB or the Hex color values of a given an HTML color name.|
|**pf_fix_path_sep.py**|[pyperclip](https://pypi.org/project/pyperclip/)|Takes path from clipboard, replaces `\` path separators with `/`, and copies new string to clipboard.|

\*Code can be altered relatively easily to remove dependency.

## [graeScript](src/graeScript) Details

- [ ] Write Details (*Sorry anyone reading this. Poor practice but really don't have time to write this out at this time.*)
