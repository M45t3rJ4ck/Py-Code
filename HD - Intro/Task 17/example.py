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


# ========= Recap on Strings ===========
# A string is a common data type which is used to represent text.
# It is a sequence of characters, such as, letters, numerals, symbols and special characters.
# You have probably already noticed what an important part strings play in programming 
# Many programs you come across will involve the manipulation of strings.
# Therefore, knowing string manipulation techniques or string handling is crucial.
# We have already touched on this subject in the previous strings task, so this will just serve as a brief recap
# and will introduce you to more advanced programs.


# ************ Example 1 ************
# Recap on slicing Strings 
print("Example 1: ")

String = 'Hello world!'
fizz = String[0:5]
print(fizz)

# Note that slicing a string does not modify the original string.
# You can simply store the  substring 'sliced' from the original string in a separate variable.
# By storing the substring in another variable, you keep the original string intact.


# ========= String Methods ===========
# String methods are built in code that perform certain operations on Strings.
# You were introduced to these methods in the previous Strings task.
# These methods very are useful as the save you from having to write the same code over and over again in order to perform a specific operation.

# Some useful String methods are as follows:
#   - string.upper()                --->    converts lowercase letters to uppercase
#   - string.lower()                --->    converts uppercase letters to lowercase
#   - string.replace("old" , "new") --->    replaces all occurrences of substring old with the substring new
#   - string.strip('char')          --->    removes leading and trailing characters 'char'
#   - string.split('delimiter')     --->    splits string according to delimiter string and returns list of substrings
#                                           ( A delimiter can be a single character or string that identifies the beginning or the end of a string.
#                                           If no value is given it will automatically split the string by white spaces.)


# ========= Note on Lists ===========
# If you noticed, the split method above returns a list
# A list is a datatype that can be thought of as a container that holds a number of other items, such as Strings, Integers or Floats.
# A list is created by placing all the items inside a square bracket [ ] and separating them by commas.
# For example, a list of Integers can be created as follows:
# int_list = [1, 2, 3, 4]
# To add an item to the end of your list, you use the append method.
# For example list.append(item) adds the single item within the brackets to the end of list
# You will learn more about lists later on in this course.


# ************ Example 1 ************
print("Example 1: ")

fact1 = "The original name of windows was Interface Manager."
fact1 = fact1.upper()
print(fact1)
fact1 = fact1.lower()
print(fact1)

# ************ Example 2 ************
print("Example 2: ")

sentence = "ThisHELLOisHELLOrandomHELLOtextHELLOweHELLOareHELLOgoingHELLOtoHELLOsplitHELLOapart"
splitSentence = sentence.split("HELLO")
print(splitSentence)

# Notice how a list is printed out?

# ************ Example 3 ************
print("Example 3: ")

fact2 = "          The$first$electronic$computer$ENIAC$weighed$more$than$27$tons.          "
fact2 = fact2.replace("$", "WOW!")
print(fact2)
fact2 = fact2.strip()
print(fact2)
fact2 = fact2.split("WOW!")
print(fact2)



# ========= Escape Character ===========
# Python uses the backslash (\) as an escape character
# The backslash (\) is used as a marker character to tell the compiler/interpreter that the next character has some special meaning.
# The backslash together with certain other characters are know as escape sequences 

# Some useful escape sequences can be found below:
# \n    -   Newline      
# \t    -   Tab         
# \s    -   Space

# The escape character can also be used if you need to include quotation marks within a string.
# You can put a backslash (\) in front of a quotation mark so that it doesn’t terminate the string.
# You can also but a backslash in front of another backslash if you need to include a backslash in a string.


# ************ Example 4 ************
print("Example 4: ")
people = "Person 1 \nPerson 2"
print(people)
# Notice the line break between the two words. The \n character is invisible - it's a command to insert a new line.


# ************ Example 5 ************
print("Example 5: ")
wage = "Person 1: \t R123.22"
print(wage)
# Notice the tab between the two words. The \t character is invisible - it's a command to insert a new tab space. 

# ************ Example 6 ************
print("Example 6: ")
sentence = "\"The escape character (\\) is a character which invokes an alternative interpretation on subsequent characters in a character sequence.\"" 
print(sentence)
# Notice that the quotation marks and backslash are printed out as part of the string.



# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===


# ================= Compulsory Task 1 ==================
# Create a program  called “alternative.py” that reads in a sting and makes each alternate character an Uppercase character
# and each other alternate character a lowercase character.

# ================= Compulsory Task 2 ==================
# Write a Python program called “counting.py” to count the number of characters (character frequency) in a string. 
# Store each letter followed by the number of occurrences in a list and print it out. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# ================= Compulsory Task 3 ==================
# Write a program called “seperation.py” which inputs a sentence and displays each word of the sentence on a separate line.

# ================= Compulsory Task 4 ==================
# Write a Python program called “disappear”  to strip a set of characters from a string.
# Ask the user to input a string and then ask the user which characters they would like to make disappear.                                                                                                            
# For example: The quick brown fox jumps over the lazy dog.                                                                                      
# After stripping a,e,i,o,u                                                                                                         
# Th qck brwn fx jmps vr th lzy dg.  

# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Create a program that determines whether a String is a palindrome.
# A palindrome is a string which reads the same backwards as forward.
# Some examples of palindromes are: racecar, dad, level and noon
# Ask the user to enter a word and check if that word is a palindrome.
# If it is a palindrome, print out 'Your word is a palindrome'.
# If it is not a palindrome, print out 'Your word is not a palindrome'.



