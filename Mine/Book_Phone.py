from tkinter import *
import tkinter as tk

top = tk.Tk()
tex = tk.Text(master=top)
tex.pack(side=tk.RIGHT)
bop = tk.Frame()
bop.pack(side=tk.LEFT)


def numbers(name, number):
    numbers = {name, number}
    return numbers


def print_numbers(numbers):
    for x in numbers.keys():
        s = "Contact Name: {} & Number: {}\n".format(x, numbers[x])
        tex.insert(tk.END, s)
        tex.see(tk.END)


def add_number(numbers, name, number):
    return lambda: numbers(name, number)


def lookup_number(numbers, name):
    if name in numbers:
        return "The number is " + numbers[name]
    else:
        return name + " was not found"


def remove_number(numbers, name):
    if name in numbers:
        del numbers[name]
    else:
        print(name, "was not found")


def load_numbers(numbers, filename):
    in_file = open(filename, "r")
    for line in in_file:
        line = line.rstrip('\n')
        name, number = line.split(",")
        numbers[name] = number
    in_file.close()


def save_numbers(numbers, filename):
    out_file = open(filename, "w")
    for x in numbers.keys():
        out_file.write(x + "," + numbers[x] + "\n")
    out_file.close()


def print_menu():
    tk.Button(bop, text="Print Phone Numbers", command=print_numbers(numbers)).pack(fill=X)
    tk.Button(bop, text="Add a Phone Number", command=add_number(numbers, name, number)).pack(fill=X)
    tk.Button(bop, text="Lookup a Phone Number", command=lookup_number(numbers, name)).pack(fill=X)
    tk.Button(bop, text="Remove a Phone Number", command=remove_number(numbers, name)).pack(fill=X)
    tk.Button(bop, text="Load File Name", command=load_numbers(numbers, filename)).pack(fill=X)
    tk.Button(bop, text="Save File Name", command=save_numbers(numbers, filename)).pack(fill=X)
    tk.Button(bop, text="Quit", command=top.destroy).pack(fill=X)


phone_list = {}
menu_choice = 0
print_menu()
while True:
    menu_choice = int(input("Type in a number (1-7): "))
    if menu_choice == 1:
        print_numbers(phone_list)
    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        add_number(phone_list, name, phone)
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = input("Name: ")
        remove_number(phone_list, name)
    elif menu_choice == 4:
        print("Lookup Number")
        name = input("Name: ")
        print(lookup_number(phone_list, name))
    elif menu_choice == 5:
        filename = input("Filename to load: ")
        load_numbers(phone_list, filename)
    elif menu_choice == 6:
        filename = input("Filename to save: ")
        save_numbers(phone_list, filename)
    elif menu_choice == 7:
        break
    else:
        print_menu()

print("Goodbye")
top.mainloop()