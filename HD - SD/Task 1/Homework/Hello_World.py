fname, lname, age = input("Please enter your Name, Surname and Age: ").split()
HW = "Hello World!"
Q1 = " "
age = int(age)
fname = str(fname)
lname = str(lname)
Q1 = input("Howzit {} {} are you {} years old? ".format(fname, lname, age))
print(HW)
