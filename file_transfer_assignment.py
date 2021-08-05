

import shutil
import os

path = 'C:/folderA'
# List files and directories

print("Before copying file:")
print(os.listdir(path))

#set where the source of the files are
source = 'C:/FolderA/html_file.txt'

#set the destination path to folder B
destination = 'C:/FolderB/html_file_copy.txt'

dest = shutil.copyfile(source, destination)

print("After copying file:")
print(os.listdir(path))

print("Destination path:", dest)
