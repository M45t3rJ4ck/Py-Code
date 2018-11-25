
# ************* HELP *****************
#  REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON HELP@HYPERIONDEV.COM, OR CREATE A NEW TEXT FILE IN THIS FOLDER CALLED 'HELP'
#  Visit www.hyperiondev.com and login to see all the ways you can get help.
# *************************************

# *** IF YOU DID NOT INSTALL NOTEPAD++ AND PYTHON (VERSION 2.7.3 or 2.7.5) ***
# *** PLEASE STOP READING THIS NOW, OPEN THE INSTALLERS FOLDER IN THIS DIRECTORY, RUN BOTH FILES TO INSTALL NOTEPAD++ AND PYTHON. ***

# Now that you have ensured that you installed Notepad++, PLEASE ENSURE YOU OPEN THIS FILE IN NOTEPAD++ otherwise you will not be able to read it.
# Right click this file --> Edit with Notepad++. Do not use Notepad or any other program to open this file for now.
# Once in Notepad++, click 'View' on the top toolbar and check 'Word Wrap'. 
# Things should be much easier to read now and comments will not go off your screen.

# Please read all the comments in this example file and all others. 

# ========= Welcome to the Hyperion Intro to Programming Micro Degree ========= 
# Welcome to the Python programming course for people with no background in programming!
# This is the start of a course in programming. 
# Python is one of the easiest languages to learn how to program with. Programming takes patience and practice, and we hope to guide you through this with our course.


#Ways of comparing things 
#As a programmer, it's important to not forget the basic logical commands.
#We can check if values or values stored in variables are equal, smaller than one another, enough or different, etc.
#These work well with if statements to control what goes on in our programs.


#The four basic comparative logic operators are greater than, less than, equal to and not with the respective symbols of  >,<,== and !.
#We can combine the greater than, less than and not operator with the equals operator and form three new operations.
#The three new operations,as you might guess, are greater than or equals to, less than or equals to or not equals with symbols of >=, <= and != respectively.


#A tip to remember it is to word out the condition. Say the condition out loud if you need to and it will naturally come to you through practice.


#Example:

num1 = 10
num2 = 20


if num1 >= num2: # The symbol for 'bigger than or equal to' is >=
    print("It's not possible that 10 is bigger than or equal to 20.")
elif num1 <= num2: # The symbol for 'less than or equal to' is <=
    print ("10 is less than or equal to 20.")
elif num1 != num2: # The symbol for 'not equal to' is !=
    print ("This is also true since 10 isn't equal to 20, but the elif statement before comes first and is true so Python will execute that!")
elif num1==num2 : # The symbol for 'equal' is ==
    print ("Will never execute this print statement...")


#'elif' stands for else if, it is a shorthand approach to having to write out else and if statements completely with wasted text.


#Explanation of how the program runs:
#So the program will check the first part of the if statement (is num 1 bigger than or equal to num 2?).
#If it is not, then it goes into the first 'elif' statement and checks if num1 is less than or equal to num2.
#If it is not then it goes into the next 'elif' statement...etc.


#To have an elif you must have an if above it.
#To have an else you must have an if or elif above it. 
#You can't have an else without an if - think about it!
#You can have as many elif under an if, but only one else right at the bottom. It's like the fail-safe statement that executes if the other if/elif statments fail!


#We can compare Strings in the following manner:


myName = "Tom"


if myName == "Tom":
    print ("Hey tom!")
	
#Q: What if my program's if condition needs two or more conditions? 
#A: We can have multiple conditions, it is quicker than writing an if statement within an if statement(nested if statements) or using and else if statement to make
    #your program work in a certain way.


#Q: How?
#A: How we normally speak and think on a daily basis, it will include conditions whether or not you realise it (See what I did here?)
#In a real-life example, if there are eggs and there is enough money to buy eggs, then you can buy eggs. Otherwise you can't.
#This is an example of a conjunction operation where both conditions need to be true for the whole statement to be true.  This is called the 'and' operation.
#Another real-life example, if your friends are at the cinema or if the hot-dogs are among the best at the cinema, then you will go to the cinema, otherwise you won't.
#This is a disjunction operation where at-least one of the conditions need to be met for the whole statement to be true. This is also called the 'or' operation.


#Example of an AND condition:


myFavouriteColour = "orange"


if myName == "Tom" and myFavouriteColour == "orange": 
    print ("Your name is Tom and your favourite colour is orange.")
else:
    print ("Your name isn't Tom or your favourite colour isn't orange.")


#If myName is Tom and myFavouriteColour is orange, then the if statement's print statement will execute. Both conditions need to be met otherwise the else statement
    #and its subordinate will execute.
	
#Example of an OR condition:


item = "chair"

if item == "dog" or len(item) == 5:
    print ("Either item is a dog, or the len of your item is 5.")




#We also have the concept of branching where the first condition that is true will be executed irrespective of whether or not the the subsequent conditions are true
    #and the subsequent conditions are skipped anyway.


#An example is this:


if item == "dog" or len(item) == 5:		#Branch 1
    print ("Either item is a dog, or the len of your item is 5.")
elif item =="chair" and len(item) == 5:	#Branch 2
    print ("Your item is both a chair and len of item is 5.")
	
#When you run the above code, what will be the output? Run this program and find out!
#Remember only one branch of the if statement will execute, even if multiple branch conditions are 'true'.


#Operators
#Data type that can use it

#Addition
#+
#Integer, real

#Subtraction
#-
#Integer, real

#Multiplication
#*
#Integer, real

#Division
#/
#Integer, real
#Integer division

#Div
#Integer
#Remainder after division

#Mod
#Integer

#Concatenation
#+
#String





