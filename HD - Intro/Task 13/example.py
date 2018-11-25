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


# ============= while Loops ==================
# A loop is a sequence of statements that are continually repeated until a certain condition is met.
# One of the simplest loops is the while loop.
# Like an if statement a while loop tests a condition, but instead to executing the code once, a while loop runs until its condition becomes False.
# In other words, the statements are repeatedly executed "while" the condition is true.


# In Python, the general syntax for a while loop is as follows:
# while conditionIsTrue:
#     executeTheseStatements


# ************ Example 1 ************
i = 9

while i < 10:
   i = i + 1
# The above loop will only execute once because the condition while i < 10 is not true after you have added 1 to i.


# ************ Example 2 ************
print("Example 2: ")
i = 0

while i < 100:
        print (i)
        i = i+1
# The above loop will print out all the numbers from 0 to 99, and then terminate.

# ************ Example 3 ************
print("Example 3: ")
i = 100

while i < 50:
        print (i)

# The above while loop will not execute at all, because i is already bigger than 50.


# ************ Example 4 ************
print("Example 4: ")
a=0

while a < 10:
        print(a)
        a += 1       # a += 1 is equivalent to a = a + 1


# Initially a is set to 0.
# The while loop then checks the condition (a < 10) to see if it is true.
# If it is true the indented statements following the while loop are executed
# So if a is less than 10, the value of a is printed and then increased by one.
# The loop then begins again by checking the the condition and determining whether to execute the indented statements.
# This goes on until the condition becomes False.


# ============= Infinite Loops ==================
# A while loop runs the risk of running forever if the condition never becomes False.
# A loop that never ends is called an infinite loop.
# Creating an infinite loop is not desirable, so you should make sure that your loop condition eventually becomes False and you loop is exited.
# You can do this by using a variable such as a in the previous example. This variable is incremented with every iteration (each time the statements within the loop
#are repeated)
# By incrementing the variable the condition should at some point become False and the loop will exit.
# While loops are know as event-controlled loops as iterations continue until some non-counter-related condition (event) stops the process.


# ************ Example 5 ************
# The following example, shows a program whose while-statement sums successive even integers (2 + 4 + 6 + 8 + ...), until the total is greater than 250.
# An update statement increments i by 2
# so that it becomes the next even integer.

print ("Example 5: ")
sum1 = 0
i=0                  #initial even integer for the sum
while sum1 <= 250:
        sum1 += i
        i += 2
        print (sum1)



# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===
        


# ================= Compulsory Task 1 ==================
# Create a new file called while.py
# Write a program that always asks the user to enter a number.
# When the user enters the negative number -1, the program should stop requesting the user to enter a number,
# The program must then calculate the average of the numbers entered excluding the -1.
# Make use of the while loop repetition structure to implement the program.
# Compile, save and run your file.

# ================= Compulsory Task 2 ==================
# Modify your while.py file to do the following:
#     - Require the user to enter their name, with only a certain name being able to trigger the loop.
#     - Print out the number of tries it took the user before inputting the correct name.
#     - Add a conditional statement that will cause the user to exit the program without giving the average of the names entered if, they enter a certain input.
# Compile, save and run your file.


# ================= BONUS Optional Task  ==================
# Create a new file in this folder called Optional_task.py
# Ask the user to enter a number less than 100.
# If they enter one above 100, ask them to try again (and continue to do so until they follow instructions).
# Once they have entered a valid number, check if it is even and if it is then multiply it by 2 and print it out.
# If it isn't, then multiply it by 3 and print it out.










