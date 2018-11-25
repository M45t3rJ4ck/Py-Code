from tkinter import *
import tkinter.filedialog as tkfd


root = Tk()
root.filename = tkfd.askopenfile(initialdir="/", title="Select File: ", filetypes=("Text Files", "*.txt"))
print(root.filename)
