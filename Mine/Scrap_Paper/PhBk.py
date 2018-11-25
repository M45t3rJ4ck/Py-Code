from tkinter import *
import tkinter as tk
import tkinter.filedialog as tkfd

root = Tk()


def numbers(name, number, tex):
    return lambda: print_number(name, number, tex)


def print_number(name, number, tex):
    tex.insert(tk.END, "Contact Name: {} & Number: {}\n".format(name, number, tex))
    tex.see(tk.END)


name = list()
number = list()
phone_list = {}
top = tk.Tk()
tex = tk.Text(master=top)
tex.pack(side=tk.RIGHT)
bop = tk.Frame()
bop.pack(side=tk.LEFT)
tk.Button(bop, text="1. Print Phone Numbers", command=print_number(name, number, tex)).pack(fill=X)
tk.Button(bop, text="Quit", command=top.destroy).pack(fill=X)
top.mainloop()
