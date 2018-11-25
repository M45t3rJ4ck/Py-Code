#Welcome to the example file for your next task.
#Now that you've completed the basic introduction to Python and completed a program correctly I am assuming you know how to create, run, edit python files correctly.
#I also hope you are able to google and use the python documents to find certain information out. This is a programmers greatest tool.
#Our teachers are of course still completely willing to help you!

#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM, OR CREATE A NEW TEXT FILE IN THIS FOLDER CALLED 'HELP'
# Visit www.hyperiondev.com and login to see all the ways you can get help.
#*************************************

#This example.py will teach you about String handling in Python, files, and functions.
#You will need to use knowledge from Task 1 as these are the fundementals of programming and techniques found in Task 1 apply to almost every programming language -> So dont be afraid to refer back!
 
#==== Indexing Strings ====
# We introduced Strings in an earlier task, as well as lists. But there's a link between them.
# A 'String' is actually a list of characters. The word 'dog' is basically formed by stringing up d, o, and g into one word. 
# You can extract the characters of a String, as if that String was a list of characters. For example:  

 
word = "Hello"
print word[0] #Prints 'H'
print word[0:] #Prints 'Hello' - ie, all the characters from the 0th position (the start of the string) to the end.
 
#A string can be indexed EXACTLY like a Python list because a string is basically a list of characters! 
 
print word [1:2] #Useful for string manipulation. Remember you can even index by variables as long as they are ints.
index = 2
print word [1:index] #Prints 'e'
 
#==== Concatenating Strings ====
# You can add, or 'concatenate' strings together to form a sentence or logner word. 
name = "Tim"
sentence = "My name is " + name

#You cannot add a string and a non string together, you must convert the non string if you want to do this: 
age = 12
sentence = "And my age is " + str(age)  #Casting int to String

# If you try run code that adds a string with a non-string, you will get an error. 
# You'll see many examples in our code where we have to cast things to a String to print them out.

# Remember that you can run this file to see output, or copy and paste sections of it into your own python files and run them to understand the code better. 

 # ===== Defining multiline strings ==== 
 # Sometimes, it's useful to have long strings that can go over one line.
 # We use triple single quotes to define a multi-line string, as follows:

longString = ''' This is a long string
 using triple quotes preserves everything inside it as a string
 even on diffrent lines and with different /n spacing. '''


#==================================================================================================

# ======== Functions =========== #
# There are times when programmers find that they often have to execute the same piece of code.
# For example, if you wrote several lines of code to define logic that given a file name, opened that file, read the contents, and printed it out to the screen, it may be useful to 'save' that code somewhere so you could easily reuse it.
# A programmer would define a function, named something like 'read_file', that would encode this logic.
# That way, the next time they need to read the contents of a file they simply "Call" the function 'read_file' which will "Return" the result of that function, which in this case is the output to be printed out to the screen.
# Functions are also sometimes referred to as 'Methods' (if you have used Java before, functions in Python are very similar to Java methods).
# Functions in programming also relate to mathematical functions - perhaps you recall f(x) in mathematics. A mathematical function took some input, in this case x, did some computation with it, and returned a value, normally called y. 
# ie y = f(x) is a function that when called with the parameter x returns the value y.
# In programming, read_file(fileName) is a function that when called with a variable stored in the value fileName, returns some value or achieves some computation.
# Without knowing it, you've already used functions. The 'write' command used above, ie ofile.write(name+"\n") is in fact a function implemented by some programmer that tells Python how to write the content you give it to the file ofile.
# There are thousands of functions already implemented in Python and its libraries that you can use to get things done - programmers have already written the logic for many common or even complex tasks, and sometimes you can find the exact function that you need to complete a task.

# This may be a bit abstract, so let's look at how you can define your own functions.


#==== Defining functions ====== #
# A function is defined as follows:

def addone(x):
    y = x+1
    return y

# This function is called 'addone', it takes as input 'the parameter x'.
# The code indented under 'def addone' is the logic of a function. It defines what happens when the function is called.
# Simply put, the function computes a new variable y, which is the value stored in variable x with 1 added to it.
# It then 'returns' the value y. 

# Note the 'def' keyword. Python knows you're defining a function when you put this in front of a word. It will expect a function name, its input parameters, and then a colon, with the logic of the function indented underneath.
# Note the 'return' keyword. Python will expect this at the end of your function, but it doesn't always have to be there. More on this later.

# If you 'called' this function with the value of x = 10, it would look exactly like this:

num = 10
numPlusOne = addone(num)

print "10 plus 1 is equal to: " + str(numPlusOne)

#Or even:

print "10 plus 1 is equal to: " + str(addone(num))

#Think of that 'call to the function', ie addone(num) , as a 'placeholder' for some computation. The function will go off and run its code, and return its result in that place.

#==== Where do functions go? ====== #

# A major switch has happened when we introduced functions. Before, all your programs were sequential. This means that whatever code was written in a file executed from the top of the file to the bottom.
# With functions, we lose this. You can define a function anywhere in your file, BUT IT WILL NOT RUN UNLESS 'CALLED' SOMEWHERE IN THE CODE.
# For example, though we have defined the function 'addone' above. The code underneath it would never be executed unless there was another line that 'called' addone with the command addone(some_variable) SOMEWHERE IN THE MAIN BODY OF YOUR CODE.
# In the next task, you'll explore Object Orientated Programming that will explain these concepts further.

#==== More function examples ====== #

def double_this_number(number):
	y = number*2 #Multiples the number by 2
	return y

def return_first_letter_word(word):
	y = word[0]
	return y

def put_number_in_list(num):
	newList = []
	newList.append(num)
	return newList

def put_number_in_list_if_big(num):
	newList = []
	if num >100:
		newList.append(num)

	return newList #Be careful! This could return an empty list.

def compute_sum_of_two_numbers(num1,num2):
	y = num1+num2
	return y

def takes_no_parameters():
	y = "This function takes no parameters as input, but that means its functionality is limited...."
	return

# As you can see from the examples above, you can pretty much do anything you want in a function.
# You can create new data structures, use conditionals etc.
# We can call the input variable anything we want. Its just a name we give it so we know how to refer to it within the function. 
# As seen in the second to last example, we can have multiple input parameters too. There's no limit on them, as long as you can keep track of what's what!
# In the last example, we have a function that takes no input parameters. This is also possible, but it means the user who calls the function has limited interaction with the function - they cant supply any input!
# In the case of some functions - imagine a function that returned the current time ie - getTime() - it makes sense to see why they need no input parameters (unless you had a more complex function like get_time(timezone) which returned the time for a timezone the calling user provides!)
# Within the body of the function, the variables passed in through num1 and num2 will be referred to them through those new variables. Think of it as copying in the values from the inputted variables.


# While the above functions may not seem useful, this is because they are so simple. You can have functions with hundreds of lines that do complex tasks.


#======================= Play around with Python a bit (OPTIONAL TASK) ============================
# Create a new python file in this folder called funcpractice.py 
# Inside in, create a function called addthree, that takes as input three parameters - num1, num2, num3
# Then, write logic to create a new variable, y, that is the sum of all three of these numbers.
# Then, return the result y.
# Now, after you've defined this function, write a function call to return the sum of the numbers 52, 25, and 1403.
# Store this result in a variabel called sumFunc
# Print out sumFunc. Don't forget to cast to a String!
#==================================================================================================

#==== A function that doesn't return anything ====== #


def print_word(word):
	print word 

# The function above just prints out something, it doesn't have a return statement
# That's okay, but it means if you make a call like:

y  = print_word("abc")

# y will store the special value None. This is not a String or any other datatype, so will cause an error when trying to do other things with it.
# Be careful that your functions return values, if that's what you need them to do.


#==== THe power of functions ====== #

#We can call the function multiple times in a loop:

num = 10
for i in range(10):
    num = addone(num)  #Runs 10 times, each time, 1 is added to the value of 10. So after the first iteration it will be 11, the second computes 11+1 = 12, etc... until 20.
	
print num

#==================================================================================================

# We mentioend earlier that there are thousands of already written functions, but how do you get access to them?
# MODULES are the answer. Modules, or libraries, are pieces of code already written by other programmers that you can 'import' into your program.
# Though you don't see the code of them directly, you can access them as follows: 
 
# === Importing outside modules ===

# Python has a huge number of modules that you must import to use. An example of this is the math module which has prebuilt in functions for you to use

import math #Imports the Math module. You do not need to install the Math module, it comes with Python but must be specifically imported into a program that uses it.

# Say you want to find the square root of a number. It would be tedious to try write code to implement that (and a bit hard if you think about it!).
# Let's just use the 'sqrt' function already implemented by some programmer years ago in the math library.
 
number = 25
print "The square root of 25 is : " + str(math.sqrt(25))   #We are using the sqrt function of the math module

# Math.sqrt returns a FLOAT which is just an int that has decimal places (for example, 1.5). 
# That makes sense, given that the square root of numbers isn't always a simple integer. The square root of 100 may be 10, but the square root of 3 has many decimal digits. 
# We must thus convert the result of math.sqrt(25) to a string before we will be able to print it out, since the print function only works on Strings.
# This explains why we have str(____) around the call to the function. 'The result of the sqrt function is being cast from float to String and printed out'

# The math library has many, many methods/functions. To find out more about them, you'd have to search something like 'math module Python' in Google to find various different function calls, what inputs they take, and what they output.
# These function calls are usually documented on webpages or guides. Python modules and their functions are usually very well documented online.

# If you want to square a number, the math module has a function, 'pow' that takes two numbers as input - the first is your number you want to square, and the 2nd is the number you want to raise your number to.
# Squaring is the same as raising to the power of two.

square = math.pow(5,2) #the pow function will take the first argument (5) and put the second argument (2) as an exponent to the number. So we get 5^2 here which is 25.

print "5 squared is equal to: " + str(square)

#======================= Play around with Python a bit (OPTIONAL TASK) ============================
# Create a new python file in this folder called squareme.py 
# Inside in, import the math python math module right at the top
# Now define a simple function inside squareme called square, that takes in a variable called 'number'
# How to do this?  remember to define a function you type 'def functionname(nameOfVariableToTakeIn)
# Then indented under that what you want to do with the variable.
# Take the variable and apply the math.pow method to it
# So math.pow(number, 2) should return the squared number right? Print it out!
#==================================================================================================

#==================================================================================================

#======= Working with files in Python ===== #

# Files are an important source of information in Python. Before moving on, we want to amke sure you know how to read and write to the most simple type of files - textfiles - using Python.
# Python includes a built-in file type. This is a bit like a String data structure, but much more complex. 

# The line below creates a new file 'object' named f that is linked to the example.txt file in this folder. You'll learn about objects in a later task.

f = file('example.txt', 'r+')
# This means f is open for reading. The first argument (example.txt.) is the filename and the second parameter is the
# mode, which can be 'r', 'w', or 'r+', among some others. r is for reading online, w is for writing online and r+ is for both. 
# Notice the way this is written is similar to calling a method 'file' with two input parameters, as described above - behind the scenes, this is exactly what is happening.


# Here we intend to read and write from example.txt, which is already in the same folder as this file, example.py. Python will look in this director for 'example.txt', and try read its context.

#The most common way to read from a file is simply to loop over the lines of the file:

f = open('example.txt', 'r+')

# We can directly loop over the variable f, which is stored in Python as a list of lines - each line is 1 line of the file. 

for line in f:
	print "The first character of this line is: " + line[0] + "\n"
	print "The entire line is: " + line


f.close() #Always close files when done with them, using this function call. Notice this is a function that takesn o input.

# We could build up all lines of the text file into a large string called contents as follows:

contents = ""

for line in f:
	contents = contents + line

f.close() #Always close files when done with them.

# We now have the contents of an external resource (a textfile), stored inside our program in a variable called contents. That's pretty powerful! But for now, let's just print the contents to a screen:

print contents

#======================= Play around with Python a bit (OPTIONAL TASK) ============================
#	Create a new python file in this folder called reader.py
#	There is already a textfile in this document called 'example.txt'. 
#   Write a very short program that creates a new file object called reader that opens the file 'example.txt' in r+ mode (should take 1 line)
#   Now that have you created the file object 'reader' add a line to your code under that that says 'print reader' 
# 	The textfile does not print out, rather you get a text outprint of something in <   >
#   This is because you printed out the OBJECT 'reader'. 'reader' is an object of the Python File class and objects and classes in Python work the same as they do in Java.
#   If you don't understand, don't worry, just understand that to print the contents of the file you have to type 'print reader.readlines()
#   Add 'print reader.readlines()' to your code and run it and you should see the contents of the file printed out!
#   When you see the output of 'print reader.readlines()' you may notice that each line is displayed in a LIST in the outprint (ie it has [   ] around it)
#   This is because Python automatically stores each line of the textfile in a list for you
#   Try adding 'print reader.readlines()[0]' to your code and now check the output. 
#   Do you understand what's happening? reader.readlines() returns a list. We automatically index to the first element in the list by adding [0] after readlines(). Then we print it out!
#   Its the same as working with lists in Task 1. When we had list = ['A','B']  print list[0] outprinted the first item of the lie - 'A'!
#==================================================================================================

#======== Writing to a file =========== #
# Let's see how to create a new text file, and write data to it.

ofile = open('output.txt', 'w') #We create a new file called output.txt (it doesn't exist yet) in write mode. Python will create this file in the directory/folder that our program is automatically. 

name = raw_input("Enter your name: "); #We ask the user for their name. When they enter it, its stored as a String in the variable name.

ofile.write(name) #We use the write function to write the contents of the variable name to the text file, which is represented by the object (a special type of variable you will learn more about later) ofile.

#You must run this python file for the file 'output.txt' to be created with the output from this program in it :)

ofile.write("My name is on the line above in this text file.") #We write to the file again and the current contents of the file will not be overwritten. instead, it will be written on the 2nd line of the text file.

ofile.close() #Dont forget to close the file!


#======================= Play around with Python a bit (OPTIONAL TASK) ============================
# Let's try write a simple program that uses a while loop to print things to a text file.
# Remember how in ap revious task you wrote a program that takes in names while the user hasnt entered 'John'?
# Remember how it stored all 'incorrect' names in a list?
# Let's take all those incorrect names and write them to a new txt file called 'IncorrectName.txt'.
# Copy and paste your code from John.py in Task 1 into this folder into a new python file called JohnWrite.py. Your Task 1 Folder may have been moved to the 'Completed Work' folder.
# At the end of your code, write the single line to create a new textfile in this folder called 'wrotenames.txt'. Don't know how to do this? Look at the section above -> we just told you how which python code creates a new file 'output.txt' in write mode :P
# Now loop through the list of incorrect names using a for loop. ie 'for name in names' if your list was saved in a variable called names.
# for each name, write the name to the text file!
# Remember to close your file afterwards!
#==================================================================================================


#======================= Play around with Python a bit (OPTIONAL TASK) ============================
# Now that you've learnt about functions and text file, there's an exciting oppertunity to link these two concepts together.
# Earlier, we introduced functions with an example of reading text files.
# Create a new program, called 'readtextfile.py', that defines inside it a function that takes as an input parameter 'filename'.
# Now, have this function attempt to read the contents of the file called 'filename', and print out those contents to the screen.
# Watch out! A filename should have it's extension too, for example, we have put an example text file in this folder called 'example'. But it's actually called 'example.txt', because the .txt extension is what tells your computer 
# that this is a text file. Your function should take in its input parameter the FULL filename, so not just 'example', but 'example.txt' if you want to try read from this file.
#==================================================================================================

 
 #==================================================================================================
 #==================================================================================================
 
 # ===== End of example code ====

#'Now you should have all the tools you need to complete this task.
		
		
# =================== TASK INSTRUCTIONS ===================================

#Read example.py. Open it using Notepad++. This should help you understand more advanced Python. You are not required to read the entirety of AdditionalReading.pdf , it is purely for extra reference. 

#This example deals with using Python to read and write files and also how to define Python functions which are similar to Java methods.

#Now, create a python file called forgetful.py . Imagine your friend was very forgetful and always seemed to enter his email password incorrectly. You want to write a python program that takes all his incorrect password entries, stores it in a list, then records 
#all his incorrect password entries in a textfile called wrongpasswords.txt. 

#Example: your friends password is 'rusty'. But he enters 'rusty123', 'Rusty', 'rustless' before finally remembering his password is 'rusty' and entering it correctly.

#In this situation wrongpasswords.txt should read this exactly:
#Incorrect password 1: rusty123
#Incorrect password 2: Rusty
#Incorrect password 3: rustless
#Correct password entered on 4th entry.

#The program should ask the user for input by saying 'Please enter your password'. You can use code from the program you wrote in Task 1. The correct password will always be 'rusty' but the user can of course enter any String.
#Good luck!


#****** OPTIONAL CHALLENGE:  ********
#Edit your completed program so that the number of characters your friend gets wrong is also stored for each incorrect password. 

#In the same situation given above, wrongpasswords.txt should read this exactly:
#Incorrect password 1: rusty123 , wrong by 3 characters. 
#Incorrect password 2: Rusty , wrong by 1 characters. 
#Incorrect password 3: rustless , wrong by 4 characters. 
#Correct password entered on 4th entry.

#You should define a seprate function in your code, called countDifference, that takes in a String and returns an int. 
#Bonus points for people who can find and import python modules to help them do this task quicker -> surely someone has written a function for finding the difference between strings already?
#But maybe it's easier to write new logic for this than have to go and find our which module has such a function defined? Who knows!

