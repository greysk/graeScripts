#! python3
# Import modules and write comments to describe this program.
import os

from PIL import Image

from graeScript import shared_out_dir

file = open(shared_out_dir / 'photo_folders.txt', 'w')
for foldername, subfolders, filenames in os.walk('U:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not filename.endswith('.png') and not filename.endswith('.jpg'):
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        im = Image.open(os.path.join(foldername, filename))

        # Check if width & height are larger than 500.
        if im.width > 500 and im.height > 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1
    if numPhotoFiles == 0:
        continue
    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numNonPhotoFiles == 0 or (
            numPhotoFiles * 2 > numNonPhotoFiles + numNonPhotoFiles):
        file.write(foldername + '\n')
