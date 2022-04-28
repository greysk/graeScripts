from pathlib import Path
import filecmp

folder1 = Path().home()
folder2 = Path('')

for file1 in folder1.iterdir():
    for file2 in folder2.iterdir():
        if filecmp.cmp(file1, file2) is True:
            print('Same files:')
            print(f'\t{file1}', f'\t{file2}', sep='\n')
