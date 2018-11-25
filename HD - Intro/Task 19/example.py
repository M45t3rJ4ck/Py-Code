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


# =========== Writing to Files in Python ===========
# Until now, your programs have been using the print statement to display output to your screen.
# We now want to write to the most simple type of file, text files, using Python.
# Just like when reading from a file, when we want to write to a file we need to open it first. 
# Also like when reading from a file, the file needs to be closed, so that resources that are tied with the file are freed.

# =========== Write Method ===========
# You can use the write() method in order to write to a file.
# The syntax for this method is as follows:
#   file.write("string")   - writes "string" to the file 

# ************ Example 1 ************
# Before you can write to a file you need to open it.
# You open a file using Python's built in open() function which creates a file called output.txt (it doesn't exist yet)
# in write mode.
# Python will create this file in the directory/folder that our program is in automatically. 

ofile = open('output.txt', 'w')

# We ask the user for their name. When they enter it, it is stored as a String in the variable name.
name = input("Enter your name: ") 

# We use the write method to write the contents of the variable name to the text file, which is represented by the
# object ofile.
# Remember, you will learn more about objects later but for now, think of an object as similar to a real-world object
# such as a book, apple or car that can be distinctly identified.
ofile.write(name+"\n") 


# You must run this Python file for the file 'output.txt' to be created with the output from this program in it.
ofile.write("My name is on the line above in this text file.")
# When we write to the file again, the current contents of the file will not be overwritten.
# The new string will be written on the second line of the text file.

ofile.close() # Don't forget to close the file!

# ****************** END OF EXAMPLE CODE ********************* #
# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===



# ================= Compulsory Task ==================
# We will write a program that allows students to register for an exam venue.
# First ask the user how many students are registering.
# Create a for loop that runs for that amount of students
# Each loop asks for the student to enter their ID numbers.
# Write each of the ID numbers to a Text File called “RegForm.txt”
# This will be used as an attendance register that they will sign when they arrive at the exam venue

# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Create a text file called "numbers1.txt" that contains Integers which are sorted from smallest to largest.
# Create another text file called "numbers2.txt" which also contains Integers that are sorted from smallest to largest.
# Write the numbers from both files to a third file called "allNumbers.txt"
# All the numbers in "allNumbers.txt" should be sorted from smallest to largest.



