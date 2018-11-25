""""Import Libraries"""
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = Tk()

numbers = {"name": "number"}


class PhoneBook:
    """PhoneBook"""

    def __init__(self, numbers, name, number):
        self.name = name
        self.number = number
        self.numbers = numbers

    def print_number(self, numbers):
        for name in list(numbers):
            Entry(root, text="Name: {} \tNumber: {}".format(name, numbers[name])).grid(row=1, column=1, sticky=W, padx=4)

    def add_details(self, numbers):
        name = Entry(root, text="Name and Surname", width=100).grid(row=1, column=1, sticky=E, pady=4)
        number = Entry(root, text="Phone Number", width=100).grid(row=4, column=1, sticky=E, pady=4)
        numbers[name] = number
        return numbers

    def remove_number(self, numbers, name):
        if name in list(numbers):
            del numbers[name]
        else:
            return name, " was not found"

    def lookup_number(self, numbers, name):
        if name in list(numbers):
            return "The number is " + numbers[name]
        else:
            return name, " was not found"

    def load_numbers(self, numbers):
        filename = askopenfilename(initialdir="C:/Python/PyCode/Mine/",
                                   filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                                   title="Choose a file name to load")
        in_file = open(filename, "r")
        for line in in_file:
            line = line.rstrip('\n')
            name, number = line.split(",")
            numbers[name] = number
        in_file.close()

    def save_numbers(self, numbers):
        filename = asksaveasfilename(initialdir="C:/Python/PyCode/Mine/",
                                     filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                                     title="Choose a file name to save")
        out_file = open(filename, "w")
        for x in list(numbers):
            out_file.write(x + "," + numbers[x] + "\n")
        out_file.close()

    def quit(self):
        root.destroy()


title = Label(root, text="...Welcome to the Phone Book Main Menu...").grid(row=0, column=0, sticky=W, padx=4)
Button(root, text="Print Phone Numbers", command=PhoneBook.print_number(numbers)).grid(row=1, column=0, sticky=W, padx=4)
Button(root, text="Add a Phone Number", command=PhoneBook.add_details(numbers)).grid(row=2, column=0, sticky=W, padx=4)
Button(root, text="Remove a Phone Number", command=PhoneBook.remove_number(numbers)).grid(row=3, column=0, sticky=W, padx=4)
Button(root, text="Lookup a Phone Number", command=PhoneBook.lookup_number(numbers)).grid(row=4, column=0, sticky=W, padx=4)
Button(root, text="Load numbers", command=PhoneBook.load_numbers(numbers)).grid(row=5, column=0, sticky=W, padx=4)
Button(root, text="Save numbers", command=PhoneBook.save_numbers(numbers)).grid(row=6, column=0, sticky=W, padx=4)
Button(root, text="Quit", command=PhoneBook.quit()).grid(row=7, column=0, sticky=W, padx=4)


root.mainloop()
