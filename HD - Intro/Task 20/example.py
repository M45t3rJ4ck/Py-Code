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


# ================= Consolidation Task ==================
# Everything you have been learning has been tested with application tasks for each section.
# Now however, you will now be utilising everything you have learnt so far to solve this problem.
# You've covered all the necessary content to solve a large real-life data problem.
# Data management is an extremely important component of the Computer Science field and this task will provide you with first hand experience.
# You may find it helpful to revise what you've learnt from your previous tasks.
# This task will also require you to do some individual research as this is an essential component to being a successful software developer.
# You now have all the tools for the compulsory task.


# ================= File Input and Output ==================

# ************ Example 1 ************
# Write a file
out_file = open("test.txt","w")
out_file.write("This Text is going to out file\nLook at it and see!")
out_file.close()

# ************ Example 2 ************
# Read a file
print("\nExample 2:")
in_file = open("test.txt","r")
text = in_file.read()
in_file.close()
print(text)


# ================= The split() Method ==================


# ************ Example 3 ************
print("\nExample 3:")

print("This is a bunch of words".split())
# prints out ['This', 'is',  'a',   'bunch', 'of', 'words']

text = "First batch, second batch, third, fourth"
print(text.split(","))
# prints out ['First batch', ' second batch', ' third', ' fourth']


# ************ Example 4 ************
print("\nExample 4:")

text = "First batch, second batch, third, fourth"
list = text.split(",")
print(len(list))
# prints out 4

print(list[-1])
# prints out 'fourth'

list = text.split(",",2)
print(list)
print(len(list))
# prints out 3

print(list[-1])
# prints out 'third, fourth'



# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===




# ================= Compulsory Task  ==================

# After you've read and understand all of example.py, create a new Python file called amazon.py inside this folder.
# This programming problem is one posed to new software developer applicants to Amazon, the software development company you've probably bought a book or dvd from once in your life.
# Inside amazon.py, write Python code to read in the contents of the textfile 'input.txt', and for each line in input.txt.
# Write out a new line in a new text file output.txt that computes the answer to some operation on a list of numbers.

# If the input.txt file has the following:
#    min: 1,2,3,5,6
#    max: 1,2,3,5,6
#    avg: 1,2,3,5,6

# Your program should generate an output.txt file as following:


#    The min of [1, 2, 3, 5, 6] is 1
#    The max of [1, 2, 3, 5, 6] is 6
#    The avg of [1, 2, 3, 5, 6] is 3.4


# Assume that the only operations given in the input file are 'min', 'max' and 'avg', and that the operation is always followed by a list of comma separated integers. 
# Your program should handle any combination of operations, any lengths of input numbers. You can assume that the list of input numbers are always valid ints, and is never empty. 


# ================= BONUS Optional Task ==================

# Change your program to also handle the operation 'px' where x is a number from 10 to 90 and defines the x percentile of the list of numbers. For example:

# input.txt:
#    min: 1,2,3,5,6
#    max: 1,2,3,5,6
#    avg: 1,2,3,5,6
#    p90: 1,2,3,4,5,6,7,8,9,10
#    sum: 1,2,3,5,6
#    min: 1,5,6,14,24
#    max: 2,3,9
#    p70: 1,2,3

# Your output.txt should read:
#    The min of [1, 2, 3, 5, 6] is 1
#    The max of [1, 2, 3, 5, 6] is 6
#    The avg of [1, 2, 3, 5, 6] is 3.4
#    The 90th percentile of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is 9
#    The sum of [1, 2, 3, 5, 6] is 17
#    The min of [1, 5, 6, 14, 24] is 1
#    The max of [2, 3, 9] is 9
#    The 70th percentile of [1, 2, 3] is 2



