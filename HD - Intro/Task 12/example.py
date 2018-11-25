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



# ================== Consolidation Task ==================
# Now that you know more about Python it’s time to write a small useful program.
# You will be utilising everything you have learnt to create a simple Investment Calculator program.
# This task will help you strengthen your understanding of all the concepts you have encountered so far.
# Feel free to go back and revise your previous tasks, as it will help you complete this task.


# ================== Interest ==================
# Interest is the cost of using someone else's money.
# When you borrow money, you pay interest and when you lend money, you earn interest.
# Interest can either be classified as simple interest or compound interest.
# Simple interest is continually calculated on the initial amount invested, and is only calculated once per year.
# This interest amount is then added to the amount that you initially invested (known as the Principal amount). 
# Compound interest is calculated on the principal amount and also on the accumulated interest of previous periods

# ************ Example 1 ************
# An example of simple interest:
# Just say you invest R1000 at 10%.
# The first year you will earn R100 interest (R1000 * 0.10) giving you R1100.
# The next year the interest is still calculated on the principal amount (R1000) giving you another R100,
# making a total of R1200.


# ************ Example 2 ************
# An example of compound interest:
# Imagine you invest R1000 at 10% compounded once a year.
# The first year you will earn R100, giving you an Accumulated amount of R1100.
# The second year you will earn interest on the Accumulated amount (1100 * 0.10), to earn R110 interest,
# giving you R1210.


# ================== How to Calculate Interest ==================
# Simple interest rate is calculated as follows:
#   A = P(1 + r * t)
#   The Python equivalent is very similar:
#       A =P*(1+r*t)

# Compound interest rate is calculated as follows:
#   A = P(1 + r) ^ t
#   The Python equivalent is slightly different:
#       A = P* math.pow((1+r),t)

# ‘r’ is the interest rate divided by 100, e.g. if 8% is entered, then r is 0.08.
# 'P' is the initial amount deposited
# 't' is the number of years of the investment 


# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===



# ================= Compulsory Task ==================
# Create a new Python file in this folder called "InvestmentCalculator.py".
# At the top of the file include the line:
#   import math
# Ask the user to input:
#   The amount that they are depositing, stored as ‘P’.
#   The interest rate (as a percentage), stored as ‘i’.
#   The number of years of the investment. stored as ‘t’.
#   Then ask the user to input whether they want “simple” or “compound” interest, and store this in a variable called ‘interest’.
# Only the number of the interest rate should be entered - don’t worry about having to deal with the added ‘%’,
# e.g. The user should enter 8 and not 8%.
# Depending on whether they typed “simple” or “compound”, output the appropriate amount that they will get after the given period at the interest rate.
# Print out the answer!
# Try enter 20 years and 8 (%) and see what a difference there is depending on the type of interest rate!


# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Create a program that allows the user to play the lottery.
# Generate a random two digit number (between 10 and 99) this number will be the lottery number.
# Ask the user to enter any two digit number this will be the user's guess.
# Get first and second digit from the two digit lottery number.
# Get the first and second digit from the user's guess.
# Print out the generated lottery number.
# If the user's guess matches the lottery number exactly, print out "Congratulations you have an exact match, you win R10 000.00"
# (i.e. if the user enters 12 and the lottery number is 12)
# If the user's guess matches the lottery numbers, but are in the wrong order print out "Congratulations you have all digits, you win R5 000.00"
# (i.e. if the user enters 48 and the lottery number is 84)
# If the user guesses one digit correctly print out "Congratulations you have one correct digit, you win R1 000.00"
# (i.e. if the user enters 27 and the lottery number is 78)
# Else print out "Sorry no match"
# To get more information on how to generate a random number vist: https://docs.python.org/2/library/random.html

