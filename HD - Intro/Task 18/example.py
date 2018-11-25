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
 
 
 
# =========== Reading From Files in Python ===========
# Until now, your programs have been using the raw_input function to get input, which by default comes from the keyboard.
# We now want to read from the most simple type of file, text files, using Python.
# Python includes a built-in file type which is a bit like a String data structure, but much more complex.
# When we want to read from a file we need to open it first. 
# When we are done, it needs to be closed, so that resources that are tied with the file are freed.
 
 
 
# ************ Example 1 ************
# Before you can read a file you need to open it.
# You open a file using Python's built in open() function which creates a file object.
# You will learn more about objects later but for now, think of an object as similar to a real-world object
# such as a book, apple or car that can be distinctly identified.
# The line below creates a new file 'object' named f that is linked to the example.txt file in this folder.
 
f = open('DOB.txt', 'r+')
 
 
# This means f is open for reading.
# The first argument (example.txt) is the filename and the second argument is the mode.
# The mode determines the mode in which the file has to be opened.
# Some of the possible values for the mode are:
# 'r'   -       Opens file for reading only
# 'w'   -       Opens file for writing only
# 'r+'  -       Opens file for both reading and writing 
 
 
# Here we intend to read and write from/to example.txt, which is already in the same folder as this file, example.py.
# Python will look in this directory for 'example.txt', and try read its context.
 
# The most common way to read from a file is simply to loop over the lines of the file:
# We can directly loop over the variable f, which is stored in Python as a list of lines.
# Each line is 1 line of the file. 
 
# ************ Example 2 ************
print("\nExample 2: ")
for line in f:
        print("The first character of this line is: " + line[0] + "\n")
        print("The entire line is: " + line)
        
f.close() 
# Always close files when done with them, using the close() function.
# This is in order to free up the resources that the file was using.
# Notice this is a function that takes in 0 input.
 
 
# ************ Example 3 ************
# We could build up all lines of the text file into a large string called contents as follows:
 
print("\nExample 3: ")
contents = ""
f = open('DOB.txt', 'r+') # Open the file again!
 
for line in f:
       contents = contents + line
 
f.close() # Always close files when done with them.
 
# We now have the contents of an external resource (a text file), stored inside our program in a variable called contents.
# That's pretty powerful! But for now, let's just print the contents to a screen:
 
print(contents)
 
# =========== Read Method ===========
# You can also use the read method in order to read from a file.
# The syntax for this method is as follows:
# file.read(n)   -   reads n number of characters from the file, or if n is blank reads the entire file
 
 
# ************ Example 3 ************
print("\nExample 3: ")
 
f = open('DOB.txt', 'r+') # Open the file again!
newContents = f.read()
print(newContents)
 
f.close() # Always close files when done with them.
 
 
# ****************** END OF EXAMPLE CODE ********************* # 
 
 
# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===
 
 
 
# ================= Compulsory Task ==================
# Write a program that reads the data from the text file called DOB.txt and prints it out in two different sections in the format displayed below:
# Name                 
#       1. A Masinga           
#       Etc.
# Birth date
#       1. 21 July 1988
#       Etc.
 
 
# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Create a new text file in this folder called input.txt
# In the input.txt file enter some text, making sure it is at least a few lines long.
# Write a program the will count the number of characters, words and lines in the file.
# Your program should also count the number of vowels (a's, e's, i's, o's and u's) in the file.
# Print out your results.
 
 
 
 
