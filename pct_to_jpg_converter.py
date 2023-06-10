import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory

# prompt user for folders
Tk().withdraw()
pct_folder = askdirectory(title='Select folder with pct images:')
jpg_folder = askdirectory(title='Select folder to save converted jpg images:')

# check if folders exist, else create them
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# loop through all files in the pct folder
for file_name in os.listdir(pct_folder):
    if file_name.endswith('.pct'):
        # open pct image and convert to jpg
        pct_file_path = os.path.join(pct_folder, file_name)
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)
        pct_image = Image.open(pct_file_path)

        # save jpg image with maximum quality
        pct_image.save(jpg_file_path, 'JPEG', quality=100)

print(f'All pct images in {pct_folder} converted to jpg and saved in {jpg_folder}.')

#softy_plug