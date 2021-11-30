import filecmp
import csv
from graeScript import to_data_folder

with open(to_data_folder / 'duplicate_file.csv') as csvfile:
    reader = csv.DictReader(csvfile)
        

print(filecmp.cmp(file1, file2))
