#Welcome to the example file for task '4.5'.

#************* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
# Visit www.rmoola.com/advice.html for all the ways you can get free help!

#===== Functions in Python=====

#Recall from the previous task:

# A function is like a java Method, its a block of defined code that is only run when you call it.
# This is a great way to reuse code and store logic that can be called from anywhere else in the program in just one line. 

def addone(x):
    return x+1

#This function takes in a variable x and adds one to it! We hope that x is an integer...
#Return means what you will get back if you go number = addone(5) , you'll get the int 6 which is 5+1
#We can call the input variable (here x) anything we want. Its just a name we give it so we know how to refer to it within the function
#(every indented under the def addone(x) line is 'within' the function)

print (str(addone(2))) #Will print out 3 


#======================= Play around with Python a bit (OPTIONAL TASK 1) ============================
#
# Create a new python file in this folder called functionPractice.py
# Define a function, sumAll(n) that sums all numbers from to 1 to n.
# For example, calling sumAll(10) should return the answer to 1 +2+3...+10
# The function sumAll will have to use a for loop to carry out this summation, and it will have to use a sum variable that increases in value over each iteration
# of the for loop.
#
#==================================================================================================

#===== Lists =====

#Recall that we can define a list of integers as follows:

nums = [ 1, 2, 3, 4]
print(nums)
sumNums = sum(nums) #We can compute the sum of the integers using built it functions, 1+2+3+4 = 10
lenNums = len(nums)	#WE can find out how many elements are in the list like this, here lenNums stores the int 4

#What if we have a string, seperated by some standard seperator called a DELIMETER, and we want to put this String into a new list?

strNums = "1,2,3,4,5" #This is one long string, but if we got rid of the commas and put each int into its own cell in a list, we could get a list of ints, like above.
print(strNums)
newNumList = strNums.split(",")		#This is an important operation. It takes the above String, splits it using the DELIMETER , and puts each item into a new list 
print (newNumList)					#Run this program, do you see the new list?

#Unfortunately, new NumList is a list of STRINGS, ie , the elements are '1', '2', .. rather than 1, 2 
#We can't sum a list of strings, we can only sum ints. What if we wanted to find the sum of a long list of numbers? We need to cast each string to an int to do so.

#We know that we can cast from a str to an int using the int() function seen earlier. But how can we do this on each element of the list.

#===== List comprehensions =====

#List comprehensions are a powerful tool that will apply some operation to every element in a list, and then put it back into a new list.
#For example:

newNumListInts = [int(element) for element in newNumList] #We are looping over newNumList, the list of Strings we created above. For each element, we are casting it
#to an int and putting it into a new list, newNumListInts

print(newNumListInts)  #Do you see the difference?

#Now we can sum this list, since newNumListInts is a list of ints, not Strings.

print(sum(newNumListInts))

#What else can we do with list comprehensions?

doubleList = [2*element for element in newNumListInts]	#A new list, with each element double its value in the previous list.
print(doubleList)
halfList = [0.5*element for element in newNumListInts] #A new list, with each element half its value in the previous list.
print(halfList)
#List comprehensions are powerful tools - don't forget them!

#======================= Play around with Python a bit (COMPULSORY TASK 1) ============================
#
# Create a new python file in this folder called comprehend.py
# Imagine there's a really rude friend of yours, that always sends emails with all words in capital letters. 
# Your friend also doesn't know how to use a spacebar, so he seperates words with the : character.
# Imagine your friend sends the message "HI:HOW:R:U:TODAY:
# Take this message, as a string. Split it into a list of string words and make each word lowercase using a list comprehension on each element.
# Read http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python for information on how to make words lowercase.
# Now, edit the first and last word (ie the first and last element of your list) to capitalise the first letter of the sentence, and add a full stop to the end of
#the sentence.
# Print out this new intelligent sentence.
#
#==================================================================================================


#===== Switch statements in Python =====

#Imagine we have a long list of codewords. Each codeword triggers a specific function to be called.
#For example, we have the codewords 'go' which when seen calls the function handleGo, and another codeword 'ok' which when seens calls handleOk.

#We can use the following structure called a HASH TABLE to encode this:

def handleGo(x):
    return "Handling a go! " + x

def handleOk(x):
    return "Handling an ok!" + x

#This is the hash table:	
codewords = { 
  'go': handleGo,   #The KEY here is 'go' and the VALUE it maps to in the hash is handleGo (which is a function!)
  'ok': handleOk,   
}

#This hash maps STRINGS (codewords) to FUNCTIONS.

#Now, we see a codeword given to us:

codeword = "go"

#We can handle it as follows:

if codeword in codewords:
	answer = codewords[codeword]("Argument")
	print(answer)
else:
	print("I don't know what you're talking about...")

#Hash functions are general tools for mapping, and in some way mimic FUNCTIONS from MATHEMATICS (remember f(x) = x^2?)
#There are some very important applications for hash functions.

#Another hash...
codewordsTwo = { 
  'one': 1,         #The key here is the string 'one' and it has the int value 1 in the hash.
  'two': 2,         #This hash maps STRINGS (the words of numbers) to INTS (their int value)
}

print("Word to number mapper:")

word = "one"
print(codewordsTwo[word])

#Here are a ton of places they are used. Take a look - http://en.wikipedia.org/wiki/Hash_function

#======================= Play around with Python a bit (COMPULSORY TASK 2) ============================
#
#   Create a new Python file in this folder called hash.py
#   Think about three celeberaties/famous people that you know.
#   Create a hash called hotMap, where the the KEYS are the name and surname of the person (ie a String), and the VALUE for each key is either the string 'hot' or
#   'not'
#   based on whether you think that person is hot or not!
#
#   Here's my hash..
#   hotMap = {
#       'EmmaWatson': 'Hot',
#       'JustinBieber': 'Not',
#       'LeoDiCaprio': 'Hot',
#   }
#
#   What does print hotMap['EmmaWatson'] return?
#
#==================================================================================================


#===== End of example code ====

#You now have all the tools for the compulsory task.
#COMPULSORY TASK: 

'''
    After you've read and under all of example.py, create a new python file called amazon.py inside this folder. This programming problem is one posed to new
    software developer applicants to Amazon, the software development company you've probably bought a book or dvd from once in your life. Inside amazon.py, write
    Python code to read in the input of the textfile 'input.txt', and for each line in input.txt, write out a new line in a new text file output.txt that computes
    the answer to some operation on a list of numbers.

    If the input.txt file has the following:

    min: 1,2,3,5,6
    max: 1,2,3,5,6
    avg: 1,2,3,5,6

    Your program should generate an output.txt file as following:

    The min of [1, 2, 3, 5, 6] is 1
    The max of [1, 2, 3, 5, 6] is 6
    The avg of [1, 2, 3, 5, 6] is 3.4

    Assume that the only operatings given in the input file as 'min', 'max' and 'avg', and that the operation is always followed by a list of comma seperated integers.

    You should define a functions min, max and average that take in a list of integers and return the max, min or average of the list. 
    Your program should handle any combination of operations, any lengths of input numbers. You can assume that the list of input numbers are always valid ints, and
    is never empty. 


    <BONUS Optional Challenge>

    Change your program to also handle the operation 'px' where x is a number from 10 to 90 and defines the x percentile of the list of numbers. For example:

    input.txt:

    min: 1,2,3,5,6
    max: 1,2,3,5,6
    avg: 1,2,3,5,6
    p90: 1,2,3,4,5,6,7,8,9,10
    sum: 1,2,3,5,6
    min: 1,5,6,14,24
    max: 2,3,9
    p70: 1,2,3

    Your output.txt should read:

    The min of [1, 2, 3, 5, 6] is 1
    The max of [1, 2, 3, 5, 6] is 6
    The avg of [1, 2, 3, 5, 6] is 3.4
    The 90th percentile of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is 9
    The sum of [1, 2, 3, 5, 6] is 17
    The min of [1, 5, 6, 14, 24] is 1
    The max of [2, 3, 9] is 9
    The 70th percentile of [1, 2, 3] is 2

'''
