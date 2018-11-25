from tkinter import *


class PhoneBook:

    """Phone List - Contact Details"""
    @staticmethod
    def phone_list():
        contact_details = {{"f_name": "First Name"},
                           {"m_name": "Middle Name"},
                           {"l_name": "Last Name"},
                           {"dob": "Date of Birth"},
                           {"email": "Email"},
                           {"wbs": "Website"},
                           {"sll": "Social Links"},
                           {"lct": "Location"}}
        return contact_details

    """Main Menu - Options - Contact Details or Filename"""
    @staticmethod
    def main_menu():
        root = Tk()
        root.geometry("300x250+150+150")

        Label(root, text="...Welcome to the Phone Book Main Menu...").grid(row=0, column=0, sticky=W, padx=7)
        print_cd = Button(root, text="Print Contact Details").grid(row=1, column=0, sticky=W, padx=5)
        add_cd = Button(root, text="Add Contact Details").grid(row=2, column=0, sticky=W, padx=5)
        remove_cd = Button(root, text="Remove a Contact Detail").grid(row=3, column=0, sticky=W, padx=5)
        lookup_cd = Button(root, text="Lookup a Contact Detail").grid(row=4, column=0, sticky=W, padx=5)
        load_fln = Button(root, text="Load File Name").grid(row=5, column=0, sticky=W, padx=5)
        save_fln = Button(root, text="Save File Name").grid(row=6, column=0, sticky=W, padx=5)
        qut = Button(root, text="Quit").grid(row=7, column=0, sticky=W, padx=5)

        root.mainloop()
        return print_cd, add_cd, remove_cd, lookup_cd, load_fln, save_fln, qut

    """Print Contact Details"""
    @staticmethod
    def print_cd(contact_details):
        for f_name, m_name, l_name, p_number, dob, email, wbs, sll, lct in contact_details.keys():
            root = Tk()
            root.geometry("300x300+150+150")

            Label(root, text="Print Contact Details").grid(row=0, sticky=W, padx=3)
            Label(root, text="First Name: ").grid(row=1, sticky=W, padx=3)
            Text.insert(END, " {} ".format(f_name))
            Label(root, text="Middle Name: ").grid(row=2, sticky=W, padx=3)
            Text.insert(END, " {} ".format(m_name))
            Label(root, text="Last Name: ").grid(row=3, sticky=W, padx=3)
            Text.insert(END, " {} ".format(l_name))
            Label(root, text="Phone Number: ").grid(row=4, sticky=W, padx=3)
            Text.insert(END, " {} ".format(p_number))
            Label(root, text="Date of Birth: ").grid(row=5, sticky=W, padx=3)
            Text.insert(END, " {} ".format(dob))
            Label(root, text="Email: ").grid(row=6, sticky=W, padx=3)
            Text.insert(END, " {} ".format(email))
            Label(root, text="Website: ").grid(row=7, sticky=W, padx=3)
            Text.insert(END, " {} ".format(wbs))
            Label(root, text="Social Link: ").grid(row=8, sticky=W, padx=3)
            Text.insert(END, " {} ".format(sll))
            Label(root, text="Location: ").grid(row=9, sticky=W, padx=3)
            Text.insert(END, " {} ".format(lct))
            Button(root, text="Submit").grid(row=10)

            root.mainloop()
            return f_name, m_name, l_name, p_number, dob, email, wbs, sll, lct

    """Add Contact Details"""
    @staticmethod
    def add_cd(contact_details):
        for f_name, m_name, l_name, p_number, dob, email, wbs, sll, lct in contact_details.keys():
            root = Tk()
            root.geometry("300x300+150+150")

            Label(root, text="Add New Contact Details").grid(row=0, sticky=W, padx=3)
            Label(root, text="First Name").grid(row=1, sticky=W, padx=3)
            f_name = Entry(root).grid(row=1, column=1, sticky=E, pady=3)
            Label(root, text="Middle Name").grid(row=2, sticky=W, padx=3)
            m_name = Entry(root).grid(row=2, column=1, sticky=E, pady=3)
            Label(root, text="Last Name").grid(row=3, sticky=W, padx=3)
            l_name = Entry(root).grid(row=3, column=1, sticky=E, pady=3)
            Label(root, text="Phone Number").grid(row=4, sticky=W, padx=3)
            p_number = Entry(root).grid(row=4, column=1, sticky=E, pady=3)
            Label(root, text="Date of Birth").grid(row=5, sticky=W, padx=3)
            dob = Entry(root).grid(row=5, column=1, sticky=E, pady=3)
            Label(root, text="Email").grid(row=6, sticky=W, padx=3)
            email = Entry(root).grid(row=6, column=1, sticky=E, pady=3)
            Label(root, text="Website").grid(row=7, sticky=W, padx=3)
            wbs = Entry(root).grid(row=7, column=1, sticky=E, pady=3)
            Label(root, text="Social Link").grid(row=8, sticky=W, padx=3)
            sll = Entry(root).grid(row=8, column=1, sticky=E, pady=3)
            Label(root, text="Location").grid(row=9, sticky=W, padx=3)
            lct = Entry(root).grid(row=9, column=1, sticky=E, pady=3)
            Button(root, text="Submit").grid(row=10)

            root.mainloop()
            return f_name, m_name, l_name, p_number, dob, email, wbs, sll, lct

    """Remove Contact Details"""
    @staticmethod
    def remove_cd(contact_details):
        for f_name, m_name, l_name, p_number, dob, email, wbs, sll, lct in contact_details.keys():
            root = Tk()
            root.geometry("300x300+150+150")

            Label(root, text="Load by File Name").grid(row=0, sticky=W, padx=3)
            Radiobutton(root, text="First Name", value=1).grid(row=1, column=0, sticky=W)
            Radiobutton(root, text="Middle Name", value=2).grid(row=2, column=0, sticky=W)
            Radiobutton(root, text="Last Name", value=3).grid(row=3, column=0, sticky=W)
            Radiobutton(root, text="Phone Number", value=4).grid(row=4, column=0, sticky=W)
            Radiobutton(root, text="Date of Birth", value=5).grid(row=5, column=0, sticky=W)
            Radiobutton(root, text="Email", value=6).grid(row=6, column=0, sticky=W)
            Radiobutton(root, text="Website", value=7).grid(row=7, column=0, sticky=W)
            Radiobutton(root, text="Social Link", value=8).grid(row=8, column=0, sticky=W)
            Radiobutton(root, text="Location", value=9).grid(row=9, column=0, sticky=W)
            Button(root, text="Submit").grid(row=10)

            root.mainloop()
            return

    """Look-up Contact Details"""
    @staticmethod
    def lookup_cd(contact_details):
        for f_name, m_name, l_name, p_number, dob, email, wbs, sll, lct in contact_details.keys():
            root = Tk()
            root.geometry("300x300+150+150")

            Label(root, text="Load by File Name").grid(row=0, sticky=W, padx=3)
            Radiobutton(root, text="First Name", value=1).grid(row=1, column=0, sticky=W)
            Radiobutton(root, text="Middle Name", value=2).grid(row=2, column=0, sticky=W)
            Radiobutton(root, text="Last Name", value=3).grid(row=3, column=0, sticky=W)
            Radiobutton(root, text="Phone Number", value=4).grid(row=4, column=0, sticky=W)
            Radiobutton(root, text="Date of Birth", value=5).grid(row=5, column=0, sticky=W)
            Radiobutton(root, text="Email", value=6).grid(row=6, column=0, sticky=W)
            Radiobutton(root, text="Website", value=7).grid(row=7, column=0, sticky=W)
            Radiobutton(root, text="Social Link", value=8).grid(row=8, column=0, sticky=W)
            Radiobutton(root, text="Location", value=9).grid(row=9, column=0, sticky=W)
            Button(root, text="Submit").grid(row=10)

            root.mainloop()
            return

    """Load File Name"""
    @staticmethod
    def load_fln(contact_details):
        root = Tk()
        root.geometry("300x100+150+150")

        Label(root, text="Load by File Name").grid(row=0, sticky=W, padx=3)
        Label(root, text="File Name").grid(row=1, sticky=W, padx=3)
        filename = Entry(root).grid(row=1, column=1, sticky=E, pady=3)
        Button(root, text="Submit").grid(row=10)
        load_fln = open(filename, "r")
        for line in load_fln:
            line = line.rstrip("\n")
            f_name, m_name, l_name, p_number, dob, email, wbs, sll, lct = line.split(" , ")
            contact_details[f_name, m_name, l_name, p_number, dob, email, wbs, sll, lct] = f_name, m_name, l_name, p_number, dob, email, wbs, sll, lct

        filename.close()
        root.mainloop()
        return load_fln

    """Save File Name"""
    @staticmethod
    def save_fln(contact_details):
        root = Tk()
        root.geometry("300x100+150+150")

        Label(root, text="Save by File Name").grid(row=0, sticky=W, padx=3)
        Label(root, text="File Name").grid(row=1, sticky=W, padx=3)
        filename = Entry(root).grid(row=1, column=1, sticky=E, pady=3)
        Button(root, text="Submit").grid(row=10)
        save_fln = open(filename, "w")
        for f_name, m_name, l_name, p_number, dob, email, wbs, sll, lct in contact_details.keys():
            save_fln.write(contact_details[f_name, m_name, l_name, p_number, dob, email, wbs, sll, lct] + "\n")

        save_fln.close()
        root.mainloop()
        return save_fln

    """Quit TKInter - Exit Phone Book API"""
    @staticmethod
    def quit_app():
        root = Tk()
        root.quit()
        root.mainloop()


"""Call to Function"""


while True:
    menu_choice = PhoneBook.main_menu()
    if menu_choice == main_menu.print_cd():
        PhoneBook.print_cd(PhoneBook.phone_list.contact_details())
    elif menu_choice == PhoneBook.main_menu(add_cd):
        print("Add Name and Number")
        f_name = input("First Name: ")
        p_number = input("Phone Number: ")
        PhoneBook.add_cd(phone_list, f_name, p_number)
    elif menu_choice == PhoneBook.main_menu(rcd):
        print("Remove Name and Number")
        f_name = input("First Name: ")
        PhoneBook.remove_cd(phone_list, f_name)
    elif menu_choice == PhoneBook.main_menu(lcd):
        print("Lookup Number")
        f_name = input("Name: ")
        print(PhoneBook.lookup_cd(phone_list, f_name))
    elif menu_choice == PhoneBook.main_menu(lfn):
        load_fln = input("Filename to load: ")
        PhoneBook.load_fln(load_fln)
    elif menu_choice == PhoneBook.main_menu(sfn):
        save_fln = input("Filename to save: ")
        PhoneBook.save_fln(save_fln)
    elif menu_choice == PhoneBook.main_menu(qut):
        break

    print("Goodbye")


