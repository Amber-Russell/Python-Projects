from tkinter import *



f = open("html_file.txt", "a")
f.write( "<html><body><h1>Stay tuned for our amazing summer sale!</h1></body></html>")
f.close()

f = open("html_file.txt", "r")
print(f.read())




