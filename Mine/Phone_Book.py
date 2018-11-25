""""Import Libraries"""
from tkinter import *

root = Tk()
"""PhoneBook"""


def print_number(numbers):
    print("Telephone Numbers:")
    for x in numbers.keys():
        print("Name:", x, "\tNumber:", numbers[x])
    print()


def add_details():
    Label(root, text="Add New Contact Details").grid(row=0, sticky=W, padx=4)
    Label(root, text="First Name").grid(row=1, sticky=W, padx=4)
    f_name = Entry(root).grid(row=1, column=1, sticky=E, pady=4)
    Label(root, text="Middle Name").grid(row=2, sticky=W, padx=4)
    m_name = Entry(root).grid(row=2, column=1, sticky=E, pady=4)
    Label(root, text="Last Name").grid(row=3, sticky=W, padx=4)
    l_name = Entry(root).grid(row=3, column=1, sticky=E, pady=4)
    Label(root, text="Phone Number").grid(row=4, sticky=W, padx=4)
    phone_number = Entry(root).grid(row=4, column=1, sticky=E, pady=4)
    Label(root, text="Date Of Birth").grid(row=5, sticky=W, padx=4)
    date_of_birth = Entry(root).grid(row=5, column=1, sticky=E, pady=4)
    Label(root, text="Email").grid(row=6, sticky=W, padx=4)
    email = Entry(root).grid(row=6, column=1, sticky=E, pady=4)
    Label(root, text="Website").grid(row=7, sticky=W, padx=4)
    website = Entry(root).grid(row=7, column=1, sticky=E, pady=4)
    Label(root, text="Social Link").grid(row=8, sticky=W, padx=4)
    social_link = Entry(root).grid(row=8, column=1, sticky=E, pady=4)
    Label(root, text="Location").grid(row=9, sticky=W, padx=4)
    location = Entry(root).grid(row=9, column=1, sticky=E, pady=4)
    Button(root, text="Submit").grid(row=10)


def lookup_number(numbers, f_name):
    Label(root, text="Look-up Details").grid(row=0, sticky=W, padx=4)
    if f_name in numbers:
        return "The number is " + numbers[f_name]
    else:
        return f_name + " was not found"


def remove_number(numbers, f_name):
    Label(root, text="Remove Details").grid(row=0, sticky=W, padx=4)
    if f_name in numbers:
        del numbers[f_name]
    else:
        return f_name, " was not found"


def load_numbers(numbers, filename):
    Label(root, text="Load Details from File").grid(row=0, sticky=W, padx=4)
    Label(root, text="Filename Name").grid(row=1, sticky=W, padx=4)
    filename = Entry(root).grid(row=1, column=1, sticky=E, pady=4)
    in_file = open(filename, "r")
    for line in in_file:
        line = line.rstrip('\n')
        f_name, m_name, l_name, phone_number, date_of_birth, email, website, social_link, location, \
        number = line.split(",")
        numbers[f_name] = m_name, l_name, phone_number, date_of_birth, email, website, social_link, location
    in_file.close()


def save_numbers(numbers, filename):
    Label(root, text="Save Details to File").grid(row=0, sticky=W, padx=4)
    Label(root, text="Filename Name").grid(row=1, sticky=W, padx=4)
    filename = Entry(root).grid(row=1, column=1, sticky=E, pady=4)
    out_file = open(filename, "w")
    for x in numbers.keys():
        out_file.write(x + "," + numbers[x] + "\n")
    out_file.close()


def print_menu():
    title = Label(root, text="...Welcome to the Phone Book Main Menu...").grid(row=0, column=0, sticky=W, padx=4)
    print_number = Button(root, text="Print Phone Numbers").grid(row=1, column=0, sticky=W, padx=4)
    add_details = Button(root, text="Add a Phone Number").grid(row=2, column=0, sticky=W, padx=4)
    remove_number = Button(root, text="Remove a Phone Number").grid(row=3, column=0, sticky=W, padx=4)
    lookup_number = Button(root, text="Lookup a Phone Number").grid(row=4, column=0, sticky=W, padx=4)
    load_numbers = Button(root, text="Load numbers").grid(row=5, column=0, sticky=W, padx=4)
    save_numbers = Button(root, text="Save numbers").grid(row=6, column=0, sticky=W, padx=4)
    quit = Button(root, text="Quit").grid(row=7, column=0, sticky=W, padx=4)
    return title, print_number, add_details, remove_number, lookup_number, load_numbers, save_numbers, quit


phone_list = {}
print_menu()
while True:
    if menu_choice == print_number:
        print_number(phone_list)
    elif menu_choice == add_details:

         add_details(phone_list, f_name, m_name, l_name, phone_number, date_of_birth, email, website, social_link,
                    location)
    elif menu_choice == remove_number:

        f_name = input("First Name: ")
        remove_number(phone_list, f_name)
    elif menu_choice == lookup_number:

        f_name = input("Name: ")
        print(lookup_number(phone_list, f_name))
    elif menu_choice == load_numbers:

        load_numbers(phone_list, filename)
    elif menu_choice == save_numbers:

        save_numbers(phone_list, filename)
    elif menu_choice == quit:
        break
    else:
        print_menu()


print("Goodbye")
root.mainloop()

""""TK Inter
root = Tk()
Label(root, text="Description").grid(row=0, column=0, sticky=W)
Entry(root, width=50).grid(row=0, column=1)
Button(root, text="Submit").grid(row=0, column=8)
Label(root, text="Quality").grid(row=1, column=0, sticky=W)
Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
Radiobutton(root, text="Poor", value=3).grid(row=4, column=0, sticky=W)
Radiobutton(root, text="Damaged", value=4).grid(row=5, column=0, sticky=W)
Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
Checkbutton(root, text="Free Shipping").grid(row=2, column=1, sticky=W)
Checkbutton(root, text="Bonus Gift").grid(row=3, column=1, sticky=W)
root.mainloop()

def get_sum(event):
    # Get the value stored in the entries
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sum = num1 + num2
    # Delete the value in the entry
    sumEntry.delete(0, "end")
    # Insert the sum into the entry
    sumEntry.insert(0, sum)
root = Tk()
num1Entry = Entry(root)
num1Entry.pack(side=LEFT)
Label(root, text="+").pack(side=LEFT)
num2Entry = Entry(root)
num2Entry.pack(side=LEFT)
equalButton = Button(root, text="=")
# When the left mouse button is clicked call the function get_sum
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)
sumEntry = Entry(root)
sumEntry.pack(side=LEFT)
root.mainloop()
           """
