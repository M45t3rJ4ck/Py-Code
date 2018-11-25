#************* HELP *****************
#REMEMBER THAT IF YOU NEED SUPPORT ON ANY ASPECT OF YOUR COURSE SIMPLY LOG IN TO www.hyperiondev.com/support TO: 
#START A CHAT WITH YOUR MENTOR, SCHEDULE A CALL OR GET SUPPORT OVER EMAIL.
#************************************* 


# *** IF YOU DID NOT INSTALL NOTEPAD++ AND PYTHON (VERSION 2.7.3 or 2.7.5) ***
# *** PLEASE STOP READING THIS NOW, OPEN THE INSTALLERS FOLDER IN THIS DIRECTORY, 
#     RUN BOTH FILES TO INSTALL NOTEPAD++ AND PYTHON. ***
# PLEASE ENSURE YOU OPEN THIS FILE IN NOTEPAD++ OR IDLE otherwise you will not be able to read it.

# *** NOTE ON COMMENTS ***
# This is a comment in Python. 
# Comments can be placed anywhere in Python code and the computer ignores them - they are intended to be read by humans. 
# Any line with a # in front of it is a comment.
# Please read all the comments in this example file and all others.



# ========= What are Variables? ===========
# A variable is a way to store information. 
# Variables can be thought of as "containers" that hold information. 
# Variables are given descriptive names that should refer to the value which it stores.


# ========= Data types ===========
# Variables can store different types of data.
# Since different data can be used for different things, a data type classifies each different type.
# Python supports the following data types:
#	- String: consists of a combination of characters
#	- Integer: a whole number without a fractional or decimal part
#	- Float: a decimal number or number containing a fractional part 
#	- Char: a single letter, number, punctuation mark or any other special character
#	- Boolean: only stores one of two values, namely TRUE or FALSE

# When writing programs, you'll have to decide what data types or variables you will need in order for your program to do what you want it to do.
# In most cases, it will be pretty obvious - want to store someone's name? Use a String; their age? Use an integer. 


# ========= How to Declare Variables ===========
# When you declare a variable, you determine its name and data type
# In Python however you do not need to indicate the data type of the variable.
# This is because Python detects the variable's data type by reading how data is assigned to the variable.
# You use the assignment operator ‘=‘ to assign a value to a variable.

# ************ Example 1 ************
num = 2
# the variable num is assigned the integer or whole number 2, due to the presence of digits and lack of quotation marks

# ************ Example 2 ************
num2 = 12.34
# the variable num2 is assigned the float or decimal number 12.34, due to the presence of the decimal point and lack of quotation marks

# ************ Example 3 ************
greeting = "Hello, World!"
# the variable greeting is assigned the String Hello, World!, due to the presence of quotation marks ("...")

# ************ Example 4 ************
numberStr = "10"
# Watch out! Since you defined 10 within quotation marks, Python knows this is a String. It's not an integer even though we understand 10 is a number.


# ========= Changing a Value Held by a Variable  ===========
# If you want to change a value held by a variable, simply assign it another value 

# ************ Example 5 ************
num3 = 4
num3 = 5
# this changes the integer value 4 held in num3 to 5


# ========= Variable Naming Rules ===========
# It is very important to give variables descriptive names that reference the value which it stores. 
# Here are the naming rules:
#   Variable names must start with a letter or an underscore.
#   The remainder of the variable name can consist of letters, numbers and underscores.
#   Variable names are case sensitive so Number and number are each different variable names.
#   You cannot use a Python keyword (reserved word) as a variable name; a reserved word has a fixed meaning and cannot be redefined by the programmer.

# ************ Example 6 ************
# Below is an example of bad naming conventions vs good naming conventions.

myName = "Tom"              # Good variable name
variableOne = "Tom"         # Bad variable name
string_name = "Tom"         # Good variable name
h4x0r = "Tom"               # Bad variable name


# myName and string_name are examples of descriptive variables as they reveal what their functions are and what content they store.
# variableOne and h4x0r are terrible names and are not descriptive. 

# Remember that you can name variables as you please, but don't make it hard on yourself!


# ========= Casting ===========
# Casting basically means taking a variable of one particular data type and “turning it into” another data type
# To do this you need to use the following functions:
#   str() - converts variable to String
#   int() - converts variable to Integer
#   float() - converts variable to Float

# ************ Example 7 ************
# Using str() to convert an Integer to String

number = 10                     
numberStr = str(number)
print("Example 7: ")
print(numberStr)

# ************ Example 8 ************
# Using int() to convert a Float to Integer

numberFloat = 99.99
numberInt = int(numberFloat)
print("Example 8: ")
print(numberInt)

# run this example; notice that numberInt does not contain a decimal?



# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===



# ======================= Play around with Python a bit  ===========================================
# 
#         At this point, why not play around with creating variables? Press the windows Start button (in the bottom left corner of your screen), in the 'Search for programs and files' box, 
#         type 'Python (command line)' and you should see a program named exactly that pop up. Click to run the program.
#         In the black box that appears, type: 
#         
#         name = "John"  
# 
#         then press enter. Nothing happens but this Python program has remembered what you set the variable 'name' to.
#         To prove this type: 
# 
#         print name 
# 
#         and then hit enter. 'John' should be printed out by the program. 
#         If you close this black box, and open a new one and type: print name , you will get an error. This is because you were coding in the Python 'Shell' and your variables aren't saved. 
#         We write Python code statements in text editors like Notepad++ or the IDLE Python GUI so that all our variable definitions and code are saved.
#         We can then run these files as Python programs at any time we want, and we can use these programs repeatedly.
#         Keep the black box open and try out some commands as you read through this file. Try to add some numbers and variables.
#          -> you are actually writing Python code already, it's that simple!
# 
# ==================================================================================================


# ================= Compulsory Task 1 ==================
# Create a new Python file in this folder called “Variables.py” 
# Inside it, write Python code declaring and assigning values for each variable type
# Print each variable on separate lines.

# ================= Compulsory Task 2 ==================
# Create a new Python file in this folder called “details.py” 
# Use a Raw Input to get the following information from the user.
#   - Name
#   - Age
#   - House number
#   - Street name
# Print out a single sentence with the containing all the details of the user.  
# For example: 
#   This is John Smith he is 28 years old and lives at house number 42 on Hamilton Street.

# ================= Compulsory Task 3 ==================
# Create a new Python file in this folder called “conversion.py” 
# Declare the following variables:
#   - num1 = 99.23
#   - num2 = 23
#   - num3 = 150
#   - string1 = “100”
# Convert the as follows:
#   - num1 into a integer
#   - num2 into a float
#   - num3 into a String
#   - string1 into an integer
# Print out all the variables on separate lines

# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py” 
# Use raw input to get any two numbers from the user.
# Store these numbers in variables called num1 and num2.
# Now swap the these two numbers around.
# The number stored in num1 should now be stored in num2, and the number stored in num2 should now be stored in num1.
# Print out the values of num1 and num2 before the swap, and the values of num1 and num2 after the swap.


