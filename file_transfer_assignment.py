

import shutil
import os

path = '/User/Sudent/Desktop/folderA'
# List files and directories

print("Before copying file:")
print(os.listdir(path))

#set where the source of the files are
source = '/Users/Sudent/Desktop/FolderA/html_file.txt'

#set the destination path to folder B
destination = '/Users/Sudent/Desktop/FolderA/html_file(copy).txt'

dest = shutil.copyfile(source, destination)

print("After copying file:")
print(os.listdir(path))

print("Destination path:", dest)
