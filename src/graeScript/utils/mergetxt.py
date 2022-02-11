#! python3

def mergetext(file1: str, file2: str) -> set:
    """Merge two text files in which each line contains one word.

    Args:
        file1 (str): One of the files to be merged.
        file2 (str): The other file to be merged.

    Return:
        set: A sorted list of each term ending in a new line.
    """
    fl1: set = {line.strip() for line in open(file1).readlines()}
    fl2: set = {line.strip() for line in open(file2).readlines()}
    return sorted({f'{line}\n' for line in fl1 ^ fl2})
