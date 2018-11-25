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



# ========= What are Strings? ===========
# A String is a common data type which is used to represent text.
# It is a sequence of characters, such as, letters, numerals, symbols and special characters.
# In Python, strings must be written within “quotation marks” in order for the computer to be able to read it.
# The smallest possible string contains 0 characters and is called an empty string.


# ************ Example 1 ************
# Some examples of strings

name = "John Doe"
fact = "A traffic jam lasted for more than 10 days, with cars only moving 0.6 miles a day."
address = "77 Winchester Lane"
emptyStr = ""


# ========= Indexing Strings ===========
# Since a String is basically a list of characters, you can extract the characters of a String.
# Each character of a String (including blanks) is indexed by numbers starting from 0 for first character on the left. 
# The characters are also indexed from right to left using negative numbers, where -1 is the rightmost index and so on.

# ************ Example 2 ************
word = "Hello"
print ("Example 2: ")

# Indexing from 0 to 4
char1 = word[0]
char2 = word[1]
char3 = word[2]
char4 = word[3]
char5 = word[4]
print (char1)
print (char2)
print (char3)
print (char4)
print (char5)

# Indexing from -5 to -1
char1 = word[-5]
char2 = word[-4]
char3 = word[-3]
char4 = word[-2]
char5 = word[-1]
print (char1)
print (char2)
print (char3)
print (char4)
print (char5)


# ========= Slicing Strings ===========
# Slicing in Python, extracts characters from a String based on a starting index and ending index
# It enables you to extract more than one character or "chunk" of characters from a String.


# ************ Example 3 ************
print ("Example 3: ")

veryLongWord = "supercalifragilisticexpialidocious"
print (veryLongWord[0:5])         # prints out 'super',  

# ************ Example 4 ************
print ("Example 4: ")
index = 6
print (veryLongWord[index:9])     # prints out 'ali' - you can use variables as indices

# ************ Example 5 ************
# You can omit either or both of the indices
# If the first index is omitted it defaults to 0, so that your chunk starts from the beginning of the original String
# If the second index is omitted it defaults to the highest index in the string, so that your chunk ends at the end of the original String.

print ("Example 5: ")
print (veryLongWord[0:]) 
print (veryLongWord[:])
# both these statements print out all the characters from the 0th position (the start of the String) to the end.

print (veryLongWord[:9])       # prints out 'supercali'

 
# ==== Concatenating Strings ====
# You can add, or 'concatenate' Strings together to form a sentence or longer word.
# Simply use the '+' operator to join strings together 


# ************ Example 6 ************
name = "Tim"
sentence = "My name is " + name


# ************ Example 7 ************
# You cannot add a string and a non string together, you must convert the non string if you want to do this.
# If you try run code that adds a string with a non-string, you will get an error. 
# You'll see many examples in our code where we have to cast things to a String in order to print them out.

age = 12
sentence = "And my age is " + str(age)  # Casting Integer to String.

# Explanation:
# The way numbers are stored and arranged differ to the way Strings are stored. 
# In the example above, we are wanting to state that your age is 12. 
# The problem lies with the integer, how do we convert an integer to a String that can be easily joined in the String statement?
# We do this by converting the integer to a String using casting and then joining it to the desired text.

# ************ Example 8 ************
print ("Example 8: ")

sentenceTwo = "No people under the age of " + str(18)+"."
age = int(input("Enter your age: ")) 

# Explanation:
# We wish to join the number 18 as a String with another String, the result of the concatenation is stored in the variable sentenceTwo.
# In the next line, we would like input of the user's age, so we make use of the function raw_input(...) and call it with a String parameter.
# raw_input(...) is a function and a function is a series of operations used to access, perform and/or set some actions to/with data if it is needed.
# The String "Enter your age" is read by the function raw_input(...) which accesses the String given to it and prints it on the screen. 
# The next step raw_input(...) takes is to read what the user types on the keyboard. This is given back to us as a String.
# Seeing that age is a something which could increase or decrease, we can say that it should be treated like a number.
# That is why we use the int(...) function to take the user's input, and return it as a number which is then stored as such in the age variable.


# ===== Defining multi-line Strings ==== 
# Sometimes, it's useful to have long Strings that can go over one line.
# We use triple single quotes to define a multi-line String
# Defining a multi-line String preserves the formatting of the String

# ************ Example 9 ************
longString = ''' This is a long string
 using triple quotes preserves everything inside it as a string
 even on different lines and with different /n spacing. '''


# ========= The len() Function ===========
# A function is a group of statements that perform a specific task.
#  A useful function is the len("string") function which returns the length of the String


# ========= String Methods ===========
# String methods are built in code that perform certain operations on Strings 
# There are many built in String methods that can provide useful functionality to your program without extra coding.
# You are able to reuse these methods over and over again.

# Some useful String methods are as follows:
#   - string.upper()                --->   converts lowercase letters to uppercase
#   - string.lower()                --->   converts uppercase letters to lowercase
#   - string.replace("old" , "new") --->   replaces all occurrences of substring old with the substring new
#   - string.strip('char')          --->   removes leading and trailing characters 'char'            



# ************ Example 10 ************
print ("Example 10: ")

manipString = "***Welcome$to$the$world$of$programming***"

manipString = manipString.replace("$", " ")
print ("manipString.replace(""$"", " "): " + manipString)

manipString = manipString.strip('*')
print ("manipString.strip(""*""): " + manipString)

manipString = manipString.upper()
print ("manipString.upper(): " + manipString)

manipString = manipString.lower()
print ("manipString.lower(): " + manipString)

print ("len(manipString)" + len(manipString)) 


# Remember that you can run this file to see output, or copy and paste sections of it into your own Python files and run them to understand the code better. 




# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===




# ================= Compulsory Exercise 1 ==================
# Create a new Python file in this folder called “Strings.py” 
# Declare the variable called hero = “Super Man”
# Print it out in the following way:
#   S^U^P^E^R M^A^N
# Do Not use any functions to do this

# ================= Compulsory Exercise 2 ==================
# Create a new Python file in this folder called “Strings.py” 
# Save the sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog!” as a single string
# Now reprint this sentence as “The quick brown fox jumps over the lazy dog”  using the replace() function to change every “!” exclamation mark with a blank space.
# Now reprint that sentence as “THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG. using the .upper() function
# Print the sentence in reverse.

# ================= BONUS Optional Task ==================
# Let's practice some casting.
# Create a new file called "Optional_task.py". 
# Write Python code to take the name of a user's favourite restaurant and store it in a variable called favRest.
# Now, below this, write a statement to take in the user's favourite number. Use casting to store it in a variable called intFav.
# Now print out both of these using two separate print statements below what you have written. Be careful!
# Once this is working, try cast favRest to an int. What happens? Add a comment in your code to explain why this is.



