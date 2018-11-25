# Create a program  called “alternative.py” that reads in a sting and makes
# each alternate character an Uppercase character and each other alternate
# character a lowercase character.

# Collecting user input
U_string = input("Please enter your sentence to convert: \n").lower()
U_string = list(U_string)
while len(U_string) > 0:
    if len(U_string) >= 3:
        string = U_string[::2]
        string = str(string)
        U_string = string.upper()
        print(str(U_string))

input("Press enter to exit")
