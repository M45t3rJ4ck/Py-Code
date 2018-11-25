##************* HELP *****************
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



# ========= elif Statements ===========
# elif is short for else if.
# It allows you to specify a new condition to test, if the first condition is False it evaluate the next one.
# Unlike the else statement, you can have multiple elif statements in an if-elif-else statement.
# If the condition of the if statement is False, the condition of the next elif statement is checked.
# If the elif statement condition is False the condition of the next elif statement is checked, etc.
# If all the elif conditions are False, the else statement and its indented block of statements are executed. 

# In Python, if-elif-else statements have the following syntax:
# if condition1 :
#       indented Statements
# elif condition2 :
#       indented Statements
# elif condition3 :
#       indented Statements
# elif condition4 :
#       indented Statements
# else:
#       indented Statements


# ************ Example 1 ************
print("Example 1: ")
grade = int(input("Enter the kid's grade: "))

if grade >= 80:
        print("Congratulations! You have an A")
elif grade >= 70:
        print("Good job! You have a B")
elif grade >= 60:
        print("Keep it up! You have a C")
elif grade >= 50:
        print("Try a little harder next time! You have a D")
else:
        print("Oh No! You have an F")

# Run this program to see what prints out, then try changing the value of the grade variable and running it again.


# ========= Some Important Points to Note on the Syntax of if-elif-else Statements ===========
# Make sure that the if/elif/else statements end with a colon (the : symbol).
# Ensure that your indentation is done correctly (i.e. statements that are part of a certain control structure's 'code block' need the same indentation).
# To have an elif you must have an if above it.
# To have an else you must have an if or elif above it. 
# You can't have an else without an if - think about it!
# You can have as many elif under an if, but only one else right at the bottom. It's like the fail-safe statement that executes if the other if/elif statements fail!




# ************ Example 2 ************
print("Example 2: ")

if len("Hello World") > 6:
        print("This sentence is long!")
elif len("Hello World") > 3:
        print("Slightly more manageable!")
else:
        print("Easy stuff")
        

# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===


# ================= Compulsory Task ==================
# Create a Python file called “Control.py” in this folder.
# This is going to expand on the first control structure task we created.
# Write code to take in a user’s age using raw_input and store their age in an integer variable called age.
# Then check if the user’s age is over 18. If the user is over 18, print out the message “You are old enough!”
# else if they are over 16 print “Almost there”,
# otherwise print “You’re just too young!” You should use one if, one elif and one else statement to do this.

# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Create a program that calculates a person's BMI 
# Ask the user to enter their weight in kg and their height in m
# Use the formula below to calculate the user's BMI:
# BMI = (weight in kg) / ((height in m)*(height in m))
# If the users BMI is 30 or greater the user is obese 
# else if the users BMI is 25 or greater the user is overweight 
# else if the users BMI is 18.5 or greater the user is normal
# If the users BMI is  less than 18.5 the user is underweight 
# Display the users BMI and whether they are obese, overweight, normal or underweight 





