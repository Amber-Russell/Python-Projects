import os
import tkinter as tk
from tkinter import *

f = open('C:\Users\Sudent\Documents\GitHub\Python-Projects\file_transfer_assignment.py')
#wildcard in the center of html to add user input
f.close()
f = open( 'C:\Users\Sudent\Documents\GitHub\Python-Projects\file_transfer_assignment.py', "r")
print(f.read())




window = Tk()
window.geometry("500x600")
lbl_input = Label(window,text='Choose a file from Directory')
lbl_input.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)




btn_add = Button(window,width=12,height=2,text='Browse Files',command=lambda: create_html())
btn_add.grid(row=3,column=1,padx=(27,0),pady=(10,0),sticky=W)

if __name__=="__main__":
    window.mainloop()
