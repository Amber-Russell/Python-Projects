import tkinter
from  tkinter import filedialog
##import tkinter, filedialog
import shutil
import os

#path to browse files
path = 'C:/folderA'

#folder source
source = 'C:/FolderA/html_file.txt'

#where the moved folders will go
destination = 'C:/FolderB/html_file_copy.txt'

#open directory
root = tkinter.Tk()
root.directory = filedialog.askdirectory()
print (root.directory)

window_main = tkinter.Tk(className='Tkinter - TutorialKart', )
window_main.geometry("400x200")
 
def submitFunction() :
    print('Choose a file')
 
button_submit = tkinter.Button(window_main, text ="Files", command=submitFunction)
button_submit.config(width=20, height=2)
 
button_submit.pack()
window_main.mainloop()
