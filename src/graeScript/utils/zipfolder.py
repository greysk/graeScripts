#! python3
'''Copies and entire folder and its contents into a ZIP file.'''
# backup_to_zip.pr - Copies and entire folder and its contents into a ZIP file
# whose filename increments.
import os
from pathlib import Path
import zipfile


def backup2zip(folder):
    # Back up the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)  # make sure folder is absolute

    # Figure out the filename this code should use based on what files
    # already exist.
    number = 1
    while True:
        zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipfilename):
            break
        number += 1

    # Create the ZIP file
    print(f'Creating {zipfilename}...')
    backupzip = zipfile.ZipFile(zipfilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backupzip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue  # don't back up the backup ZIP files.
            backupzip.write(os.path.join(foldername, filename))

    backupzip.close()
    print('Done')


if __name__ == "__main__":
    backup2zip(Path(""))
