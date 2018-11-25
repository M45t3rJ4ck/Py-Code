
# This is a comment in python. 
# Comments can be placed anywhere in Python code and the computer ignores them - they are intended to be read by humans. 
# Any line with a # in front of it is a comment.

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

#Assigning a Boolean variable is very simple.
#You declare the variable name and then choose it's starting value.
#This value can then be changed as the program runs

PassWord = False
PassWord = True

##################
##Now that you have learnt about control statements, we will be able to use Booleans to their full potential.
##As of now we only know how to declare a boolean variable as either true or false, but how would this benefit us?
##How would we use it?

##This is where the if statement comes into play.
##Let's look at a simple decision we make in our everyday lives.
##When you are about to leave your house do you always take an umbrella?
##No, you would only take an umbrella when it is raining outside.
##This is a very rudimental example of decision making where there are only two outcome.
##We can apply these basic principles to create more complex programs.

Umbrella = "Leave me at home"
Rain = True

if (Rain == True):
   Umbrella = "Bring Me With"

print (Umbrella)
