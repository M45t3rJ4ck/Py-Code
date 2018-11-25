name = "John"
List_names = []
name = input("Please enter a name: ")
if name != "John":
    List_names.append(name)
    while name != "John":
        name = input("Please enter a name: ")
        List_names.append(name)
        if name == "John":
            print("Incorrect Names: ",List_names)
