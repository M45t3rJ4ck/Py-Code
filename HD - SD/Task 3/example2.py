#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON HELP@HYPERIONDEV.COM, OR CREATE A NEW TEXT FILE IN THIS FOLDER CALLED 'HELP'
#*************************************

#REMINDER: OPEN THIS FILE IN IDLE

#You're almost at the end of the Task!
#Hopefully, this has so far been a recap of programming skills you already know in another language.
#If not, please make sure you have done the optional programming exercises in the 'Playing around with Python' sections to reinforce your learning.

#Now that you know the basics, we will start combining several concepts to create even more powerful programs.


#============= Writing while loops ==================

#A while loop is more advanced than a for loop. Instead of specifying how many times you want it to run in advance, 
#The while loop will continue to execute until the condition is no longer true.
#You have to set up a while loop carefully because you may create an infinite loop if the condition cannot become false in the execution of the while loop!

i = 9
while i < 10:
   i = i + 1
   
# The loop will only execute once because the condition while i < 10 is not true after you have added 1 to i.

i = 0

while i <100:
	print (i)
	i = i+1

# The above loop will print out all the numbers from 0 to 99, and then terminate.

i = 100

while i < 50:
	print (i)

# The above while loop will not execute at all, because i is already bigger than 50.

# You can use any conditions in your while loops, for example:

name = 'Tom'
while name != 'John':
	name = input('Enter your name') #Asks the user to enter a new name, store what they enter in the variable name

# Remember that after each iteration of the while loop completes, the while condition will be checked again to see if the code inside the loop runs again.

# While loops are useful for validation. What if you want a user to keep inputting things until he gets something right?
# While the user has not entered the correct thing...execute some code. This will be useful in the upcoming tasks.

#======================= Play around with Python a bit (OPTIONAL) =================================
#	
#	Create a new file in this folder called firstWhile.py.
#	In it, define an integer variable called start. Store the value of 5 in it.
#	Then, create a while loop that while 'start' is not even (ie divisible by 2 with no remainder), will print out the value of 'start',
#and then add 1 to it.
#	How many times with this loop execute before stopping?
#
#==================================================================================================

#============= Infinite while loops ==================

# Create a new file called 'whileInfinite.py' in this folder, and copy and paste the code below, removing the # characters. What happens if you run this code?
i = 10
while i < 14:
   print ("I can see infinity")


# This will loop forever because the condition i < 14 will always be true because you never change i in the while loop -> be careful!



#======================= Play around with Python a bit (OPTIONAL) =================================
#	
#	Create a new file in this folder called whileNot.py
#	In your program, type 'import random' in the top line.
#	Then, type num = random.randint(1,5) 
#	Every time your program is run, num will be assigned a random integer from 1 to 5.
#	Now, get a users input and cast it to an int. Store it in a variable numGuess.
#	While numGuess is not equal to num, give the user another guess!
#	Under the while loop, type a print statement to outprint "You guessed correctly!"
#	Run your program a few times - how many tries does it take you to get it right? 
#	Extend your program to make it even harder for the user to guess the right answer.
#
#==================================================================================================


#======================= Play around with Python a bit (OPTIONAL) =================================
#
#	You've now learnt about if statements, for loops, and lists. That's a lot and those are really the bread and butter of Python.
#	Try write another simple program, called listMe.py , that takes in one user input (as a String) and then adds it to the end of a list. 
#	So our list will have one item like ['Input']
#	See if you can extend the program so that the user can enter 3 items into their list, using a for loop. 
#	Print the list out at the end to see if it’s working  and run it a few times by yourself with different input to check if it's working correctly -
#it's all about practice!
#
#	An example run of the above program is
#	Enter an item: Dog               -> Start of for loop asking for items to put into list
#	Enter an item: Cat               -> 2nd run of for loop
#	Enter an item: Harry             -> 3rd and last run of for loop
#	Your list is: ['Dog','Cat','Harry'] -> the output of the list that has had the three Strings above appended to it
#
#	From the problem description I hope you can logically see that a program like this will use: 
# 	- raw_input to get user input.
#	- a list that initially starts out as empty, but then grows as items are appended.
#	- a for OR while loop to track how many items have been added already.
#	- a print statement after the loop to print out what items have been added. !
#
#==================================================================================================


#============= Comparing Strings and else if else statements ==================  
#We can have more complicated logical structures. We can chain up multiple if statements.
#elif stands for else if. If the first condition isn't satisfied, it will check the 2nd, then the third, then if none of the top are true, it will have to execute the else.
 
name = "John"
if name == "Mary": #First check
	print ("Hello")
elif name == "Peter": #If first check fails then another check
	print ("Parker")
else:                 #If all the checks above fails
	print ("Ok :(") 
	
#You can of course only have an if statement or an if statement with as many elif's as you want or just an if-else. You cannot just have an elif or else.


#============= The difference between assigning things to variables and checking if a variable has a certain value ==================  
	
#Note that name = "John" means you are assigning the string John to name. 
#name == "Mary" means 'check if the String stored in the variable name equals "Mary" . 

# Don't confuse = and ==  ********* NB ************

#============== Nesting (Slightly more advanced thought processes) ===================

if name == "A":
		if name =="B":
			print ("It isn’t possible for this code to execute, how can the variable name be two things at once?")
else:
	print ("Your name isn’t A but I can’t automatically assume from that that it isn’t B") 
	
#Think about this one logically! Note the indentation carefully. You have an if within an if else. 

#You can also have a for within a for loop (a nested for), a while within a while -> anything you want really! 


#============== Conditionals revisited ==================

if name == "A" or name =="B":
	print ("Your name is either A or B but I don’t know for sure which!")
elif name =="A" and name =="B":
	print ("This code will never execute because name cant be both the string A and B at the same time")
	
#or is the symbol for 'OR' and and is the symbol for 'AND' which match up to logic. 
#Think about how two nested if statements is similar logic to one if statement with an AND condition! 

#======================= Play around with Python a bit (OPTIONAL) =================================
#	
# 	Write a new program, andOr.py.
#	The program should take an integer as input from the user, and generate a random integer from 1 to 10 using the command random.randint(1,5) .
#	Only using one if condition, have the program output "True" when the users integer is bigger than the random integer and another 'True' if the integer is
#also even.
#
#==================================================================================================

#======================= Play around with Python a bit (OPTIONAL) =================================
#	
# 	Write a new program, listsTwo.py
#	The program should take an integer as input. It should then allow the user to input as many Strings as the number  entered into a list of Strings.
#	For example, if the user enters 3, the program should program them three separate times for a String.
#	Once this is working, extend your program so that a user can only enter a String that isn't already in the list.
#	Think about how this can be done most efficiently. 
#
#==================================================================================================

#======================= Play around with Python a bit (OPTIONAL) =================================
#	
#	Write a new program named TomRiaz.py and save it in this folder.
#	The program should take in a users name.  Only if his name is "Riaz" OR "Tom" will it execute a for loop asking 
#	for some the user to add items to a list (similar to the above optional exercise). 
#	If the user's name was "Tom" it will print the list of all the items the user entered, if it was "Riaz" it will not print the list. 
#	This is because Riaz just tells Tom what to buy, Tom needs to see the list at the end of the program!
#	Try thinking about the logic behind if statements, OR , AND and how you can do just about anything if you use the right combination of these at the
#	right time!
#==================================================================================================

#****************** END OF EXAMPLE CODE FOR TASK 3 ********************* #

#== Make sure you have read and understand all of this example.py file.
#== Now please complete the compulsory program for this Task as specified in the 'Instructions.pdf' file in this folder ===
#== For this compulsory program you are required to create a file called John.py in this folder and complete a simple program ===
#== Make sure you create John.py in this folder so that one of our tutors can find it and mark it. ===

#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
#************* HELP *****************
