#Congratulations for making it to this task! You're well on your way to being a programmer.
#Let's explore some more complex programming ideas. If you feel you're struggling to keep up at any point - use your prior task's code to refresh your knowledge.

#Inside the 'Example programs' folder you'll find example programs to help you understand concepts discussed below.
#Please open these files in IDLE, view the code, and run them to test your understanding.
#We strongly encourage that you complete all the 'Play around with Python' sections below.

#============= Casting ==================
#Sometimes you need to convert from one variable type to another. This is called 'casting'
#The function of casting is to convert the data of a specific format to be used in another format for some operations
#Remember when we talked about what would happen if you tried to add a String variable and an int variable?
#You would get an error  known as a TypeError because they are incompatible to be added or concatenated together in different formats  


#When we want to join a number with a string to form a string, this is called concatenation 

#Example 1
number = 10
stringNumber = str(number) 
sentence = "A number divisible by two is " + stringNumber 

#Explanation:

#The way numbers are stored and arranged differ to the way strings are stored. 
#In the example above, we are wanting to state that the number is divisible by two. 
#The problem lies with the integer, how do we convert an integer to a string that can be easily joined?
#We do that be converting the number to a string then joining it with the text we desired


#Example 2
sentenceTwo = "No people under the age of " + str(18)
age = int(raw_input("Enter your age")) 

#Explanation

#We wish to join the number 18 as a string then join the string with the other string, the result of the concatenation is stored in the variable sentenceTwo
#In the next line, we would like input of the user's age so we make use of the function raw_input(...) and call it with a string parameter.
#raw_input(...) is what is termed a function and a function is a series of operations used to access, set or both while performing some actions to data if it is needed.
#The string "Enter your age" is read by the function raw_input(...) which accesses the string given to it and prints it on the screen. 
#The next step raw_input(...) takes is to read what the user types on the keyboard. This is given back to us as a string.
#Seeing that age is a something which could increase or decrease, we can say that it should be treated like a number 
#and that is why we use the int(...)  function to take the user's input, and return it as a number which is then stored in age.

#======================= Play around with Python a bit  ============================
#
#	Let's practice some casting.
#	Create a new file called 'cast.py'. Remember the tips from the prior task to make sure you're not creating cast.py.txt (Turn extensions on in Windows)
#	Now write Python code to take the name of a users favourite restaurant and store it in a variable called favRest
#	Now, below this, write a statement to take in the users favourite number. Use casting to store it in a variable called intFav
#	Now print out both of these using two separate print statements below what you have written. Be careful!
#	Now, once this is working, try cast favRest to an int. What happens? Add a comment in your code to explain why this is.
#
#==================================================================================================




#=============  Writing if statements ==================

#if statements are a type of control structure which controls the flow of logic within a program.
#Let us consider a real-life example:
#    Imagine you are wanting to attend a movie premiere and your favourite actor/actress is there, but you have homework to do.
#    So if your homework is done, then you would attend the premiere, else you would do your homework 
#In Python, we have the if statement which resembles how we would normally speak.

#Example
if age >= 18:
	print ("You're over 18 and can come in")
else:
	print ("You're to young sorry")

#Explanation:

#Before we continue, remember in casting we had some code wanting us to input an age?
#We check if the age is greater than or equal to 18, if the age meets the condition, then the person is allowed inside and if they are not 18 and older,
	#then they are too young.

#Q: Why  is there a colon at the end of the if and else statement?
#A: The colon, as in the English language, serves the purpose of adding extra information.
#    In Python, the colon means that here is code following that statement and can only run if the statement's criteria is met.

#Q: Why is the code after the colon indented? And is it important?
#A: The indentation means that the information follows from the colon and in this case we have the if statement. 
#    The indentation is there to demonstrate that the program's logic will follow that path is indicated.
#    Everything in the indentation will run if the program's if or else statement's conditions are met.

#Q: Why do we write the lines of code below each other? 
#A: The way that programs are run is done in a manner to how we humans read books or a newspaper.
#    We read from the top through to the bottom, in programming, this concept is called sequential programming
#    Sequential programming is logically ordered instructions to alter data and serve a purpose. 
#    Imagine if one of your elder family members give you random instructions? It wouldn't work very well.
#    Sequential programming is the only programming philosophy we are going follow in this course.

#Q: Why does the if statement only run once if the condition is met and the else not run?
#A: As explained above, sequential programming plays the formative role in how the programs run. 
#    In the example above, if you are 16, then the Python interpreter will see that the condition isn't met for the if statement.
#    So once the interpreter is done checking the if statement, it sees that there is the next line with the print command.
#    But that statement is indented and falls under the if statement, so it is automatically ignored.
#    The next line is the else statement, so the condition is automatically met since the if condition failed and the indented code of the else statement will run.


#So we have two important thing to note here:
#   1) Make sure that the if/elif/else statements end with a colon symbol :
#   2) Ensure that your indentation is done correctly.
#       To indent in Python, use the tab key. In IDLE, we can type the if/elif/else statements and press enter for automatic indentation.

#======================= Play around with Python a bit  ============================
#
#	Let's practice an if-else statement and indentation.
#	Let's write a simple (and useful!) program to determine is a number is even or not.
#
#	Create a new file called 'if.py'. Remember the tips from the prior task to make sure you're not creating cast.py.txt (Turn extensions on in Windows)
#	Now write Python code to take in a number a user enters. Store it in an integer variable called num, and make sure to use casting so that it's an int and not
#a String.
#	Now, a number is even if when dividing by 2 you get not remainder. For example, 3 divided by 2 is 1 remainder 1. So it is not even.
#	A command that checks a remainder is called MODULUS. In Python, you can do this with a % command. 
#	For example:
#	if num%2 == 0 :
#		<Do something>
#	
#	This means that if the number stored in variable num, modulus 2 has a remainder of 0, do whatever is indented under the if statement.
#	With this knowledge it should be easy to complete this program to output either 'The number you entered is even' or 'The number your entered is odd'.
#	Test your program with different numbers such as 3, 2, 8. Does it work?			
#
#==================================================================================================



#=============  Ways of comparing things ==================

#As a programmer, it's important to not forget the basic logical commands.
#We can check if values or values stored in variables are equal, smaller than one enough, different, etc.
#These work well with if statements to control what goes on in our programs.

#The four basic comparative logic operators are greater than, less than, equal to and not with the respective symbols of  >,<,== and !
#We can combine the greater than, less than and not operator with the equals operator and form three new operations.
#The three new operations as you might guess are greater than or equals to, less than or equals to or not equals with symbols of >=, <= and != respectively

#A tip to remember it is to word out the condition. Say the condition out aloud if you need to and it will naturally come to you through practice

#Example

num1 = 10
num2 = 20

if num1 >= num2: #The symbol for 'bigger than or equal to' is >=
	print ("It's not possible that 10 is bigger than or equal to 20")
elif num1 <= num2: #The symbol for 'less than or equal to' is <=
	print ("10 is less than or equal to 20") 
elif num1 != num2: #The symbol for 'not equal to' is !=
	print ("This is also true since 10 isn't equal to 20, but the elif statement before comes first and is true so Python will execute that!")
elif num1==num2 : #The symbol for 'equal' is ==
	print ("Will never execute this print statement...")

#'elif' stands for else if, it is a shorthand approach to having to write out else and if statements completely with wasted text.


#Explanation of how the program runs
#So the program will check the first part of the if statement (is num 1 bigger than or equal to num 2?) 
#If it is not, then it goes into the first 'elif' and checks if num1 is less than or equal to num2
#If it is not then the next...etc

#To have an elif you must have an if above it.
#To have an else you must have an if if. 
#You can't have an else without an if - think about it!
#You can have as many elif under an if, but only one else right at the bottom. It's like the fail-safe!

#We can compare strings in the following manner:

myName = "Tom"

if myName == "Tom":
	print ("Hey tom!")
	
#Q: What if my program's if condition needs two or more conditions? 
#A: We can have multiple conditions, it is quicker than writing an if statement within an if statement or using and else if statement to make your program work in a
	#certain way.

#Q: How?
#A: How we normally speak and think on a daily basis, it will include conditions whether or not you realise it (See what I did here?)
#    In a real-life example, if there is eggs and there is enough money to buy eggs, then you can buy eggs. Otherwise you can't.
#    This is an example of a conjunction operation where both conditions need to be true for the whole statement to be true.  This is called the 'and' operation
#    Another real-life example, if your friends are at the cinema or if the hot-dogs are among the best at the cinema, then you will go to the cinema, otherwise you
#won't.
#    This is a disjunction operation where at-least one of the conditions need to be met for the whole statement to be true. This is also called the 'or' operation

#Example of an AND condition:
myFavouriteColour = "orange"

if myName == "Tom" and myFavouriteColor == "orange": 
	print ("Your name is Tom and your favourite colour is orange")
else:
	print ("Your name isn't Tom or your favourite colour isn't orange")

#If myName is Tom and myFavouriteColour is orange, then the if statement's print statement will execute. Both conditions need to be met otherwise the else statement
	#and its subordinate will execute.
	
#Example of an OR condition:

item = "chair"

if item == "dog" or len(item) == 5:
	print ("Either item is a dog, or the len of your item is 5")


#We also have the concept of branching where the first condition that is true will be executed irrespective of whether or not the the subsequent conditions are true
	#and the subsequent conditions are skipped anyway.

#An example is this

if item == "dog" or len(item) == 5:		#Branch 1
	print ("Either item is a dog, or the len of charactes item is 5")
elif item =="chair" and len(item) == 5:	#Branch 2
	print ("Your item is both a chair and len of characters in item is 5")
	
#When you run the above code, what will be the output? Run this program and find out!
#Remember only one branch of the if statement will execute, even if multiple branch conditions are 'true'
	

#======================= Play around with Python a bit  ============================
#
# 	Let's practice comparing things and if statements.
#	As you can see, if-elif-else statements can be used to VALIDATE things.
#	Remember casting? Remember that you can only cast a STRING to an INT if the String is something like "18". You can't convert "ABC" to an int or you'll get an
#error.
#	Let's write a program to demonstrate how an if else statement can be used to avoid this problem - i.e. to VALIDATE user input
#	Create a program called validate.py and save it in this folder.
#	Inside, write code to take in a String from a user. Ask the user for a number. Save it in a String variable called numStr.
#	ASSUME the user only ever enters "3" , "2" or "NO".
# 	We can cast "3" or "2" to an Integer, but not "NO".
#	Write an If, elif, else statement to only cast numStr to a new variable, called numInt if it is either "3" or "2", else out-print "No can't be cast to an int'.
#	Did it work? Test your code with 3, 2 and No as inputs and comment the results.
# 	Now try other inputs - what happens?
#	
#==================================================================================================
	


#=============  Writing for loops ==================
#Programmers are lazy and sometimes they don't want to have to copy and paste the same statement many times.
#A for loop can specify patterns and repeat code.
#In this for loop below, the condition is that when the variable i (which is an integer) is in the range of 1 to 10 (i.e. either 1, 2, 3 ,4 ,5 ,6 ... or 10) , the code
#under
# the for loop will execute. range(1, 10) specifies that i = 1 in the first iteration of the loop. so 1 will be printed by this code. 
#Then the code will run again, this time with i=2, 2 will be printed out...etc. until i=10. Now i is not in the range (1,10) so the code will stop executing.
#i is known as the index variable as it can tell you what 'iteration' the loop is on.

for i in range(1, 10):
	print (i) 

#This for loop prints the numbers 1 to 9. Again, note the indentation and the colon, just like in the if statement.

#You can use an if statement within a for loop!

for i in range (1,10):
	if i > 5:
		print (i)
		
#This will only print the numbers 6, 7, 8 and 9 because numbers less than or equal to 5 are filtered out

#======================= Play around with Python a bit  ============================
#
#	Let's practice writing for loops.
#	Get user input and cast it to an int. Store it in a variable called num.
#	Now, if the number is bigger than 10, use a for loop to out-print it as many times as its value.
#	For example, if a user enters 11, the number 11 will be printed out 11 times.
#	If the user enters 6 or anything less than equal to 10, the program should out-print "Sorry, too small".
#
#	HINT: Use a for loop within an if statement.
#	HINT: You can use variables in range. ie, for i in range (1, num): 		
#
#==================================================================================================

#****************** END OF EXAMPLE CODE FOR THIS TASK ********************* #

#== Make sure you have read and understood all of the example.py file. 
#== Now please complete the compulsory program for this Task as specified in the 'Instructions' pdf file in this folder ===
#== For this compulsory program you are required to create a file called Control.py in this folder and complete a simply program ===
#== Make sure you create Control.py in this folder so that one of our tutors can find it and mark it. ===
