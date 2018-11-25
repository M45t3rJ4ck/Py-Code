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


       
# ============= for Loops ==================
# Programmers don't want to have to copy and paste the same statement over and over again.
# Just like a while loop, a for loop allows statements to be repeated a number of times
# However, unlike a while loop the number of repetitions is know ahead of time
# A for loop is a counter-controlled loop.
# It starts with a start value and counts up to an end value.

# In Python a for loop has the following syntax:
# for indexVariable in sequence:
#	statements

# As you can see the Python for loop starts with the keyword 'for' followed by a variable that will hold each of the values of the
# sequence, as we move through it.
# The indexVariable can tell you what 'iteration' the loop is on.
# In each 'iteration'(repetition) of the for loop the code indented inside the for loop is repeated.
# You can use the Python range() function to generate a sequence of numbers, which are then used to iterate through a for loop.
# The range() function needs two integer values, a start number and a stop number.
# For the function range(start, stop), the start number IS included and stop number is NOT included. 


# ************ Example 1 ************
print("Example 1: ")
for i in range(1, 10):
        print(i)

# Explanation:
# This for loop prints the numbers 1 to 9. Again, note the indentation and the colon, just like in the if statement.
# In this for loop, when the variable i (which is an integer) is in the range of 1 to 10 (i.e. either 1, 2, 3 ,4 ,5 ,6 ... or 9), the code under the for loop will
# execute. Range(1, 10) specifies that i = 1 in the first iteration of the loop.
# Through each iteration of the loop i will be increased by 1 until i is 10 and therefore not in the range (1,10).
# The loop will then stop executing.

        

# ************ Example 2 ************
# You can use an if statement within a for loop!
print("Example 2: ")
for i in range (1,10):
        if i > 5:
                print(i)
                
# This will only print the numbers 6, 7, 8 and 9 because numbers less than or equal to 5 are filtered out.




# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===



# ================= Compulsory Task 1  =================
# Save your program as "tables.py".
# This program needs to display the timetables for any number.
# For example, say the user enters 6 the program must print:
                       
#               The 6 times table is:
#		6 x 1 = 6
#		6 x 2 = 12
#                   …
#		6 x 12 = 72     
# Compile, save and run your file.


# ================= Compulsory Task 2 ==================
# A simple rule to determine whether a year is a leap year is to test whether it is a multiple of 4.
# Write a program to input a year and a number of years.
# Then determine and display which of those years were or will be leap years.
# Example:
# What year do you want to start with?           1994
# How many years do you want to check?           8

# 1994 isn’t a leap year
# 1995 isn’t a leap year
# 1996 is a leap year
# 1997 isn’t a leap year
# 1998 isn’t a leap year
# 1999 isn’t a leap year
# 2000 is a leap year
# 2001 isn’t a leap year

# Compile, save and run your file.


# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py” 
# Get user input a number and cast it to an int. Store it in a variable called num.
# Now, if the number is bigger than 10, use a for loop to output it as many times as its value.
# For example, if a user enters 11, the number 11 will be printed out 11 times.
# If the user enters 6 or anything less than equal to 10, the program should output "Sorry, too small".

