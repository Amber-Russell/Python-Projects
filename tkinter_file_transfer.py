import os
import tkinter as tk
from tkinter import *

f = open('./FolderA/file3.txt','a')
#wildcard in the center of html to add user input
f.close()
f = open( './FolderA/file3.txt', "r")
print(f.read())




window = Tk()
window.geometry("500x200")
lbl_input = Label(window,text='Choose a file from Directory')
lbl_input.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)




btn_add = Button(window,width=12,height=2,text='Browse Files',command=lambda:())
btn_add.grid(row=3,column=1,padx=(27,0),pady=(10,0),sticky=W)

if __name__=="__main__":
    window.mainloop()
