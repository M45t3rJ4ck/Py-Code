#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON HELP@HYPERIONDEV.COM, OR CREATE A NEW TEXT FILE IN THIS FOLDER CALLED 'HELP'
#*************************************

#REMINDER: OPEN THIS FILE IN IDLE.

#Congrats! You've made it to the next task.
#You've learnt the basics of programming - variables, data types, if statements, casting and loops.
#These basics are the core of all programming languages - in fact - they are all you need!
#It has been scientifically proven that anything and everything that can be possibly computed, can be computed with just these tools!

#Just like with basic tools out ancestors used (such as stone hammers/bone daggers), we have moved on to make advanced tools such as Jet Engines, Skyscrapers
#and planes... The most basic tools of computation are those you have learnt. Any language, or method that can in some way encode or carry out what you have learnt is known as TURING COMPLETE. 
#This is named after the famous Computer Scientist - Alan Turing. Alan Turing came up with the Theory of Computation - which
#proves that anything can be computed with the simple methods and tools you have used.

#Sounds crazy right? It isn't. When people study 'Computer Science', this is the core theme of the science. Why not read up about it and Turing a bit, or watch the recent movie - 'The Imitation Game' which is about Turing's life.
#You may also be interested in knowing that the human DNA has been proven to be Turing-Complete. 
#This means that any kind of computation is possible within our bodies - and even that Python has the same computational power as our own bodies.

#So why bother with learning more programming tools? Imagine having to compute everything using reactions of DNA in test tubes!
#From here on, any programming tools you learn are just for CONVENIENCE. They help make a programmers life much easier. 
#But THEORETICALLY speaking, you don't even need them!

#============= Working with lists/arrays ==================

#You have learnt about Strings, Ints and Float variables. But you can also have LISTS.
#You can have a LIST of Strings, Ints or Floats, even a combination of these.
#Lists and list operations are always specified by square brackets []. 

#Here we define a list of 3 strings. So this is a String list

stringList = ['John', 'Mary', 'Harry'] #Python knows that anything defined in [] is an array (Java) which in Python is known as a list. There are 3 String
#items in this list.

#We can dive into a list and get any element.
#In all programming languages, the first element of a list is at 0. The second is at 1 etc. 

print (stringList[0]) #prints 0th element of list, John. the 0st element of a list is also known as the first element of a list, or the 'element at index 1'.

print (stringList[1:2]) #prints everything from the 1st to the 2nd element of list, NOT including the 2nd element. So only prints the item in the 1th position
#which is Mary

print (stringList[0:]) #prints everything from the 0th position to the end ie the entire list

print (stringList) #A faster way to print the entire list 

stringList[2] = "Tom" #We can replace the 3rd element of the list with a new String. 'Harry' will be lost.

print (stringList) #To see that the list has changed

stringList.append("Cary") #We can add to the end of a list like this. This is important! We don't want to lose what is already on the list -> the safest bet is
#to just put new things on the end!

print (len(stringList)) #Will print the total number of items in the list, currently 4.


# ***** See the Example Programs folder in this directory for more examples! ***************#


#======================= Play around with Python a bit (Optional Task) ============================
#
#	Create a new Python file in this folder called 'listTypes.py'.
#	Imagine you want to store the first names of three of your friends in a list of Strings. 
#	Create a list variable called friends_names, and write the syntax to store the full names of three of your friends.
# 	Now write statements to print out the name of the first friend, then the name of the last friend, and finally the length of the list.
#	Now define a list called friends_ages, that stores the age of the each of your friends in a corresponding manner - ie the first entry of this list is the
#age of the friend named first in your other list.
#
#==================================================================================================


#**** EXTRA INFORMATION - TECHNICAL ****
# NB. LISTS are not totally like java ARRAYS. They do NOT have a fixed limit you have to set at the start! (Don't worry if you don’t know about this)
# They can dynamically resize, as you append items they just grow with no problem. As you remove, the same can happen with no errors.
# You can start off with an empty list A = [] . Then go A.append("Hi") and A will now be ['Hi']. That's really painless compared to Java!
# This is because Python 'Lists' are a more advanced 'Data Structure' than 'Arrays' in other languages --> But that's a more advanced topic!

#============= Looping over lists ==================

#What if you have a list of items and for each item you want to do something? Python is able to do this very quickly and much more easily than Java.
#Imagine if the list had 100 items, 3 items or no items. The logic is the same and can be done in one line in Python. 
print("Looping")

items = ['Milk', 'Bread', 'Cheese'] #Define a list of strings

for item in items:
	print (item) 

#This loop prints out every item in the list. 
#This is a very powerful tool in Python and shows how you can simply loop through an array/list.

numbers = [1,2,3,4]

for num in numbers:
	print (num)

#Any type of list can be looped over using this construct. The above will print out the numbers 1 to 4 - ie the entries in list 'numbers'.

#============= Using the xrange command ==================
# The xrange command is a special one in Python, that will automatically generate a list of integers for you.
# Use it as follows: 

num_till_10 = range(0,10) # This will create a list of integers =[0, 1,2,3,4,5,6,7,9] and store it in the variable 'num_till_10'

num_till_5 = range(0,5) 

num_2_till_5 = range(2,5)

#The resulting list can be looped over like any list of intergers, ie to print the numbers from 1 to 10:

for num in num_till_10:
	print (num)

#since num_till_10 = xrange(0,10), the above for loop is exactly the same as :

for num in range(0,10):
	print (num)


# ***** See the Example Programs folder in this directory for more examples! ***************#

#======================= Play around with Python a bit (Optional Task) =============================
#
#	Create a new Python file in this folder called 'loop1000.py'
#	Imagine I asked you to print out all the numbers from 1 to 1000.
#	Either you'd be up all night writing a list of integers, or you can be smart and use the range command.
#	Write 2 lines of code in your file to print out all numbers from 1 to 1000.
#	Once you've got this to work, add logic inside your loop to only print out the numbers from 1 to 1000 that are even (ie divisible by 2).
#	Remember the modulo command - ie %. 10%5 will give you the remainder of 10 divided by 5. 10 divided by 5 equals 2 with remainder of 0, hence this statement
#returns 0.
#	Any even number is a number that can be divided by 2 with no remainder.
#
#==================================================================================================


#======================= Play around with Python a bit (Optional Task) =================================
#	
#	Create a new file in this folder called loopLists.py
#	Inside it, define a list of Strings of your 5 favourite movies.
#	Now, loop over the list. For each item in the list, print out "Movie: " plus the movies name.
#	Can you figure out how to outprint Movie 1: <Movie 1's name>
#	Movie 2: ... etc?
#	HINT: YOU WILL NEED TO LOOP UP the 'enumerate' command in Python using a Google search.
#	This command allows you to loop over a list retaining both the item at every position, and its index (ie position in the list)
#
#==================================================================================================

#============= Checking if something is in a list ==================
myPets = ['parrot', 'dog', 'monkey']

# You can check if a certain item is in a list very easily:

if 'cat' in myPets:
	print ("The item cat was found in the list myPets")

# Don't foget this! This is a much quicker way than looping through all items, such as if you did:

for item in myPets:
	if item == 'cat':
		print ("The item cat was found in the list myPets")


#******************* CHECKPOINT. Please make sure you understand LISTS, FOR LOOPS, IF STATEMENTS, VARIABLES, and GETTING INPUT ******************************
#If you do not by this point, then you should go back and try complete the optional tasks above. 
#If you still feel some things are not clear, please read the attached AdditionalReading.pdf, or create a new file in your Dropbox folder called 'Help.txt'
#and write what you need help with.

#As a new programmer, the above may take you a while to get your head around - rather take the time to learn the fundamentals now than rush ahead!
#Remember that ALL programming languages have these 'structures' (if statements, for loops, lists etc). So if you can learn them now, they will apply to all other languages.
