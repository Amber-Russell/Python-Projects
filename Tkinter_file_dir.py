import tkinter
from  tkinter import filedialog
##import tkinter, filedialog
import shutil
import os

#open directory
root = tkinter.Tk()
root.directory = filedialog.askdirectory()
print (root.directory)

window_main = tkinter.Tk(className='Tkinter - TutorialKart', )
window_main.geometry("400x200")
 
def submitFunction() :
    print('Choose a file')



btn_Browse1 = Button(m, text="Browse...", padx=20, command=pickSourceDir)

btn_Browse2 = Button(m, text="Browse...", padx=20, command=pickDestDir)

 
window_main.mainloop()
