#************* HELP *****************
#REMEMBER THAT IF YOU NEED SUPPORT ON ANY ASPECT OF YOUR COURSE SIMPLY LOG IN TO www.hyperiondev.com/support TO: 
#START A CHAT WITH YOUR MENTOR, SCHEDULE A CALL OR GET SUPPORT OVER EMAIL.
#************************************

# *** IF YOU DID NOT INSTALL NOTEPAD++ AND PYTHON (VERSION 2.7.3 or 2.7.5) ***
# *** PLEASE STOP READING THIS NOW, OPEN THE INSTALLERS FOLDER IN THIS DIRECTORY, 
#     RUN BOTH FILES TO INSTALL NOTEPAD++ AND PYTHON. ***
# PLEASE ENSURE YOU OPEN THIS FILE IN NOTEPAD++ OR IDLE otherwise you will not be able to read it.

# *** NOTE ON COMMENTS ***
# This is a comment in Python. 
# Comments can be placed anywhere in Python code and the computer ignores them - they are intended to be read by humans. 
# Any line with a # in front of it is a comment.
# Please read all the comments in this example file and all others.


# ========= if-else Statements =========
# if statements are one of the most important concepts in programming, but on their own they are a bit limited.
# After the if statement you can add an else statement.
# An if statement together with an else statement is known as an if-else statement 
# The else statement represents an alternative path for the flow of logic if the condition of the if statement turns out to be False.
# If the if condition turns out to be True, the statements in the indented block following the if statement are executed. 
# If the if condition turns out to be False, the statements in the indented block following the if statement are skipped,
# and the statements in the indented block following the else statement are executed.

# In Python, the general if-else syntax is:
# if condition :
#	indented Statements
# else:
#	indented Statements

# ************ Example 1 ************
print("Example 1: ")
grade = 66

if grade >= 80:
        print ("Congratulations you have an A")
else:
        print ("You do not have an A")

# Explanation:
# If the grade is greater or equal to 80, the print statement in the indented block after the if statement is executed and "Congratulations you have an A” is printed
# If the grade is not greater or equal to 80, the print statement in the indented block after the else statement is executed and "You do not have an A" is printed 


# ************ Example 2 ************
# Variables have different types and depending on what sort of operation you wish to do on them you may need to change their type.
# The example below shows that a String value does not equal an Integer, even if they appear to be the same  
print ("Example 2: ")
if 9 == "9":                             #Comparing an integer and a string
        print ("Types matter")
else:
        print("Types don't matter")


# ************ Example 3 ************
# You can only compare data types with each other if they are the same
# To do this you need to change the type by casting.
# This is often used when the user is giving input as it is usually stored as a string.

print ("Example 3: ")
if 9 == int("9"):
        print ("Successful casting")
else:
        print ("I didn't need to cast that!")



# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===



# ================= Compulsory Task ==================
# Create a Python file called “Courier.py” in this folder.
# You need to design a program for a courier company to calculate the cost of sending a parcel.
# Ask the user to enter the price of the package they would like to purchase.
# Ask the user to enter the total distance of the delivery in km’s.
# Now add on the delivery costs to get the final cost of the product.
# There are four categories to factor in when determining a parcel’s final cost each with two options based on their delivery preferences.
#(Use an if else statement based on the choice they make)
#       - Air R0.36 per Km or freight R0.25 per Km
#       - Full insurance R50 or limited insurance R25
#       - Gift R15.00 or no gift R0.00
#       - Priority R100 or standard delivery R20
# Work out the total cost of the package based on the selection in each category.

# ================= BONUS Optional Task ==================
# Create a Python file called “Optional_task.py” in this folder.
# Design a program for a department store to calculate the monthly wage for two different types of employees.
# Employees can either be a salesperson or a manager.
# Salespeople earn a 8% commission on their gross sales and a fixed salary of R2000.00 per month. 
# Managers earn an hourly rate of R40.00.
# Determine if the user is a salesperson or a manager.
# Then, depending on their answer, calculate the monthly wage for the employee.
# If the user is a salesperson ask for their gross sales for the month.
# If the user is a manager ask for the number of hours worked for the month.
# Display the total monthly wage for the employee. 


