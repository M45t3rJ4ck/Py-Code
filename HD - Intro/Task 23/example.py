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


# ========= Functions in Python ===========
# A function is a reusable and organised block of code that is used to perform a single action or specific task.
# Functions are also sometimes referred to as 'Methods' (if you have used Java before, functions in Python are very similar to Java methods).
# Functions in programming also relate to mathematical functions; perhaps you recall f(x) in mathematics.
# A mathematical function takes some input, in this case x, does some computation with it, and returns a value, normally called y. 
# i.e. y = f(x) is a function that when called with the parameter x returns the value y.
# Functions can either be user-defined or built-in.
# Built-in functions are built into the Python language itself and are readily available for us to use.
# You have actually already been using some built-in functions such as, len(), int(), str() and float().
# There are thousands of functions already implemented in Python that you can use to get things done.
# Programmers have already written the logic for many common and even complex tasks, and sometimes you can find the exact built-in function that you need to complete
# a task.
# However, you are not limited to these functions.
# You can also create your own functions to meet your own needs, these are what are know as user-defined functions.


# =========== Importing Outside Modules ===========
# We mentioned earlier that there are thousands of already written functions, but how do you get access to them?
# MODULES are the answer. Modules, or libraries, are pieces of code already written by other programmers that you can 'import' into your program.
# Though you don't see their code directly, you can access them.
# You import these modules using the 'import' keyword followed by the module's name.
# An example of a very useful module, is the math module which has many pre-built in functions for you to use.
# To find out more about the math module and its functions, go to https://docs.python.org/2/library/math.html
# Python modules and their functions are usually very well documented online.


# ************ Example 1 ************
# Say you want to find the square root of a number. It would be tedious to try write code to implement that (and a bit hard if you think about it!).
# Let's just use the 'sqrt' function already implemented by some programmer years ago in the math library.
 
print("\nExample 1: ")
import math
# Imports the math module.
# You do not need to install the math module, it comes with Python but must be specifically imported into a program that uses it.

number = 25
print("The square root of 25 is : " + str(math.sqrt(25))+".")   # We are using the sqrt function of the math module.

# Explanation:
# math.sqrt returns a FLOAT which is just an int that has decimal places (for example, 1.5). 
# That makes sense, given that the square root of numbers isn't always a simple integer.
# The square root of 100 may be 10, but the square root of 3 has many decimal digits. 
# We must thus convert the result of math.sqrt(25) to a String before we will be able to print it out, since the print function only works on Strings.
# This explains why we have str(____) around the call to the function.
# The result of the sqrt function is being cast from float to String and printed out.


# ************ Example 2 ************
# If you want to square a number, the math module has a function: 'pow', that takes two numbers as input
# The first is the number you want to raise to a power, and the second is the power you what to raise a number to.
# Squaring a number is the same as raising that number to the power of 2.

print("\nExample 2: ")
square = math.pow(5,2)
# The pow function will take the first argument (5) and put the second argument (2) as an exponent for the first number.
# So we get 5^2 which is 25.

print("5 squared is equal to: " + str(square)+".")


# ************ Example 3 ************
print("\nExample 3: ")
import math            # This line imports the math module.
everything = dir(math) 
print((everything))

# The above code imports all content from the math module which we then simply print/list on the console to view.
# This is extremely useful when you need to import contents from modules or even other programs you've created - but we'll take a look at that later.
# dir() is another one of the many built-in functions Python has.
# This function returns all the names or attributes for the specified input parameter (here the math module). 


# =========== Some Other Useful Built-In Functions ===========
# It may be useful to know about some more built-in functions that can do work for you. 
# Examples of these can be found below.

# ************ Example 4 ************
print("\nExample 4: ")

maximum = max(1,5,7,3,6)
print(maximum)


minimum = min(1,4,7,1)
print(minimum)


absolute = abs(-42)
print(absolute)


# When you run this code, you'll notice how the functions automatically do the mathematical operation for you.



# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===



# ================= Compulsory Task ==================
# Create a new Python file in this folder called “Binary.py”
# Write a program that can convert a binary number to a decimal number.
# A binary number is basically a number that is made up entirely of 0s and 1s (e.g 101101)
# You can represent any amount you would like using binary.
# Ask the user to enter a binary number and convert that number to a decimal number.
# You can visit the following site to find out how to convert from binary to decimal:
#   http://www.rapidtables.com/convert/number/how-binary-to-decimal.htm
# Print out the decimal value of the number.
# Remember to make use of the built-in functions found in the math module as well as lists.



# ================= BONUS Optional Task ==================
# Create a Python file called "amazon.py" in this folder.
# Write code to read the content of the text file input.txt.
# For each line in input.txt, write a new line in the new text file output.txt that computes the answer to some operation on a list of numbers.
# If the input.txt has the following:
#       Min: 1,2,3,5,6
#       Max: 1,2,3,5,6
#       Avg: 1,2,3,5,6
# Your program should generate output.txt as follows:
#       The min of [1, 2, 3, 5, 6] is 1.
#       The max of [1, 2, 3, 5, 6] is 6.
#       The avg of [1, 2, 3, 5, 6] is 3.4.
# Assume that the only operations given in the input file are min, max and avg, and that the operation is always followed by a list of comma separated integers.
# You should define the functions min, max and avg that take in a list of integers and return the min, max or avg of the list.
# Your program should handle any combination of operations and any length of input numbers.
# You can assume that the list of input numbers are always valid integers and that the list is never empty.

