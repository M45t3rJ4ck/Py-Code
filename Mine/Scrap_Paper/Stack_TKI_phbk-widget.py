import tkinter as tk


def cbc(name, number, tex):
    return lambda: print_number(name, number, tex)


def print_number(name, number, tex):
        s = "Name and Surname: {} \tNumber: {}\n".format(name, number)
        tex.insert(tk.END, s)
        tex.see(tk.END)


def name():
    tk.Entry(top, width=50).grid(row=0, column=1)


def number():
    tk.Entry(top, width=50).grid(row=1, column=1)


top = tk.Tk()
tex = tk.Text(master=top)
tex.pack(side=tk.RIGHT)
bop = tk.Frame()
bop.pack(side=tk.LEFT)
tk.Button(bop, text="Print Contact", command=print_number(name, number, tex)).pack()
tk.Button(bop, text="Exit", command=top.destroy).pack()
top.mainloop()
