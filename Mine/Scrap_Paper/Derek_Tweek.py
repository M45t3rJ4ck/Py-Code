from tkinter import *
from tkinter import ttk, messagebox

numbers = {"Riaan Voges": "074 578 1454", "Voges Home": "021 903 9845", "Henk Voges": "076 890 5143"}


# ---------- TKINTER PHONE BOOK  ----------
def phone_list(number):

    # Get the value stored in the entries
    name = str(nameEntry.get())
    surname = str(surnameEntry.get())
    get_number = name + " " + surname

    # Index the number using name&surname
    for number in numbers:
        if get_number in numbers:
            number = numbers[get_number]
        else:
            number = "Contact Unknown"

    # Delete the value in the entry
    get_numberEntry.delete(0, "end")

    # Insert the number into the entry
    get_numberEntry.insert(0, number)


def add_phone(number):

    # Get the value stored in the entries
    name = str(nameEntry.get())
    surname = str(surnameEntry.get())
    set_number = str(get_numberEntry.get())
    get_number = name + " " + surname
    numbers[get_number] = set_number

    # Delete the value in the entry
    get_numberEntry.delete(0, "end")

    # Insert the number into the entry
    get_numberEntry.insert(0, number)


root = Tk()

nameEntry = Entry(root)
Label(root, text="Name").grid(row=0, column=0)
nameEntry.grid(row=1, column=0)
addButton = Button(root, text="+")
addButton.bind("<Button-2>", add_phone)
addButton.grid(row=1, column=1)
surnameEntry = Entry(root)
Label(root, text="Surname").grid(row=0, column=2)
surnameEntry.grid(row=1, column=2)
equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", phone_list)
equalButton.grid(row=1, column=3)

# When the left mouse button is clicked call the function get_number
get_numberEntry = Entry(root)
Label(root, text="Phone Number").grid(row=0, column=4)
get_numberEntry.grid(row=1, column=4)

root.mainloop()
