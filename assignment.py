import os
import tkinter as Tk
from tkinter import *
import webbrowser 

def create_html():
    try:
        os.remove("html_file.html")

    except:
        None
    #x is to retrieve user input
    x = txt_input.get()

    f = open("html_file.html", "a")
    #wildcard in the center of html to add user input
    f.write( "<html>\n\t<body>\n\t\t<h1>{}</h1>\n</body>\n</html>".format(x))
    f.close()
    f = open("html_file.html", "r")
    print(f.read())
    #open in browser
    webbrowser.open('html_file.html', new=1)

    
window = Tk()
window.geometry("500x500")
lbl_input = Label(window,text='Enter a sentence:')
lbl_input.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)


txt_input = Entry(window,text='')
txt_input.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)


btn_add = Button(window,width=12,height=2,text='HTML',command=lambda: create_html())
btn_add.grid(row=3,column=1,padx=(27,0),pady=(10,0),sticky=W)



if __name__=="__main__":
    window.mainloop()
