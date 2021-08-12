import tkinter
from tkinter import *
import tkinter.filedialog 
import shutil
import os

#pick a folder from directory 
def pick_sourcedir():
    my_dir = tkinter.filedialog.askdirectory()
    source_dir.delete(0, END)
    source_dir.insert(0, my_dir)

#sends files from source directory to destination
def pick_destination():
    my_dir = tkinter.filedialog.askdirectory()
    destination_dir.delete(0, END)
    destination_dir.insert(0, my_dir)


def file_move():
    source = source_dir.get()
    destination = destination_dir.get()
    source_files = os.listdir(source)
    for i in source_files:
        shutil.move(source + '/' + i, destination)


m = tkinter.Tk()
m.minsize(750, 150)

#Browse button and its geometrical location
btn_Browse1 = Button(m, text="Browse...", padx=20, command=pick_sourcedir)
btn_Browse1.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

#entry for the source directory
source_dir = Entry(m, width=100)
source_dir.grid(row=0, column=1, padx=20, pady=(30, 0), sticky=E)

#second button to browse to put the files in a new location
btn_Browse2 = Button(m, text="Browse...", padx=20, command=pick_destination)
btn_Browse2.grid(row=1, column=0, padx=(20, 10), pady=10)

destination_dir = Entry(m, width=100)
destination_dir.grid(row=1, column=1, padx=20, pady=(20, 0), sticky=E)


btn_check = Button(text="Check for files...", pady=10, command=file_move)
btn_check.grid(row=2, column=0, padx=(20, 10), pady=(0, 15))






m.mainloop()
