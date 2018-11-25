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


# ============= Nested Loops ==================
# Now that you have experience using loops we are going to consolidate that knowledge by introducing you to Nested Loops.
# A nested loop simply put is a loop within a loop.
# Each time the outer loop is executed, the inner loop is executed right from the start.
# That is, all the iterations of the inner loop is executed with each iteration of the outer loop. 

# ************ Example 1 ************
# The syntax for a nested for loop in another for loop is as follows:
# sequence =[]
# for iterating_var in sequence:
#   for iterating_var in sequence:
#      statements(s)
#   statements(s)

# ************ Example 2 ************
# The syntax for a nested while loop in another while loop is as follows:
# while condition:
#    while condition:
#       statement(s)
#   statement(s)

# ************ Example 3 ************
# You can put any type of loop inside of any other type of loop.
# For example, a for loop can be inside a while loop or vice versa.

# sequence =[]
# for iterating_var in sequence:
#    while condition:
#       statement(s)
#   statements(s)

# ************ Example 4 ************
# This example prints out the first 5 multiples of numbers 1 to 5

print("Example 4: ")

for x in range(1, 6):
    for y in range(1, 6):
        print('%d * %d = %d' % (x, y, x*y))
    print("")

# Run this program to see the output

# ============= Nested if Statements ==================
# You can also nest if statements either within another if statement or within a loop

# ************ Example 5 ************
# Nested if statements
print("Example 5: ")
name = "B"
if name == "A":
        if name =="B":
                print("It isn't possible for this code to execute, how can the variable name be two things at once?")
else:
        print("Your name isn't A but I can't automatically assume from that that it is B.")
        
# Think about this one logically! Note the indentation carefully. You have an if within an if and then an else.



# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===



# ================= Compulsory Task =================
# Create a new Python file in this folder called “TriTable.py.” 
# Write a program that uses nested for loops to create the following number pyramid.

# 1
# 2     4       
# 3     6       9
# 4     8       12      16
# 5     10      15      20      25
# 6     12      18      24      30      36
# 7     14      21      28      35      42      49
# 8     16      24      32      40      48      56      64
# 9     18      27      36      45      54      63      72      81

# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Create a program to check if a number inputted by the user is prime.
# A prime number is a positive integer greater than 1, whose only factors are 1 and the number itself.
# Examples of prime numbers are: 2, 3, 5, 7, etc.
# Ask the user to enter an integer.
# First check if the number is greater than 1.
# If it is greater than 1, check to see if it has any factors besides one and itself.
# i.e if there are any numbers between 2 and the number itself that can divide the number without any remainders 
# If the number is a prime number, print out the number and ' is a prime number!'
# If the number is not a prime number, print out the number and ' is not a prime number'



