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



# ============= What are Lists? ==================
# The list is a datatype, just like strings, integers and floats.
# Lists are written as a list of values (items), separated by commas, between square brackets [].
# The values or items in a list can be strings, integers, floats or even other  lists or a mix of different types..


# ============= Creating a Lists ==================
# To create a list simply put different comma-separated values between square brackets.
# A list can have any number of items and they may even be of different types.
# It can even have another list as an item.

# ************ Example 1 ************
# A List of Strings

stringList = ['John', 'Mary', 'Harry']
# Python knows that anything defined in [] which in Python is known as a list.
# There are 3 String items in this list.

# ************ Example 2 ************
# A List containing different datatypes

mixedList = ['Hello', 3.4, 89, 'World']

# ************ Example 3 ************
# A List containing another List

myList = ['Monkey', 'Elephant', [3, 4, 6, 10]]


# ============= Indexing Lists ==================
# We are able to access all elements in a list using the index operator [].
# The index starts from 0 for the leftmost item, so a list having 10 elements will have indices from 0 to 9.
# Alternatively the index can begin with -1 for the index of the rightmost item, so a List having 10 elements will have indices from -10 to -1.
# Indices must be integers.
# This is very similar to how you would access individual characters in a String.


# ************ Example 4 ************
print("Example 4: ")

petList = ['cat', 'dog', 'hamster', 'goldfish', 'parrot']

print(petList[0])
# Prints 'cat'.
# The element at position 0 is also known as the first element of a list, or the 'element at index 0'.

print(petList[-2])
# Prints 'goldfish'
# The element at position -2 is also known as the 4th element of the list, or the 'element at index -2'. 


# ============= Slicing Lists ==================
# You can slice lists in the same way as you would slice Strings.
# We can access a range of items in a list by using the slicing operator (colon).
# In order to slice a list you need to indicate a start and end position of the items you would like to access.
# You place these positions between the index operator [] and separate them with the colon.
# The item in the start position is included in the sliced list, while the item in the end position is not included.

# ************ Example 5 ************
print("\nExample 5: ")

numList = [1, 4, 2, 7, 5, 9]

print(numList[1:2])
# Prints everything from the 1st to the 2nd element of list, NOT including the 2nd element.
# So it only prints the item in the 1st position.

print(numList[0:])
# Prints everything from the 0th position to the end of the list i.e. the entire list.

print(numList)
# A faster way to print the entire list. 


# ============= Changing Elements in a Lists ==================
# Elements in a list can be changed.
# You use the assignment operator (=) to change single or multiple elements.

# ************ Example 6 ************
print("\nExample 6:")

nameList = ['James', 'Molly', 'Chris', 'Peter', 'Kim']
nameList[2] = 'Tom'
# We can replace the 3rd element of the List with a new String.
# 'Chris' will be lost and replaced with 'Tom'. 
print(nameList) # To see that the List has changed.

nameList[1:4] = ['Joe', 'Lucy', 'Kelly']
# We can replace the 2nd, 3rd and 4th elements of the List with a new String.
print(nameList) # To see that the List has changed.


# ============= Adding Elements to a Lists ==================
# You can add an element to the end of a List using the 'append()' method.

# ************ Example 7 ************
print("\nExample 7:")

newList = [34, 35, 75, 'Coffee', 98.8]
newList.append('Tea')
# Adds the String 'Tea' to the end of the List
print(newList)


# ============= Deleting Elements From a List ==================
# You can use the 'del' keyword to delete one or more items from a List.
# You are even able to delete the List entirely.

# ************ Example 8 ************
print("\nExample 8:")

charList = ['P', 'y', 't', 'h', 'o', 'n']

del charList[3]
# Deletes the single element 'h'
print(charList)

del charList[1:3]
# Deletes multiple elements from the 2nd to 4th element.
print(charList)

del charList
# Deletes the entire List


# ============= Getting the Length of a List ==================
# You can get the length of the List (how many elements there are in the list) by using the len() function.
# This is the same function we used to get the length of a string. 

# ************ Example 9 ************
print("\nExample 9:")

oddNumList = [1, 3, 5, 7, 9]
print(len(oddNumList))
# Will print the total number of items in the list, currently 5.



# **** EXTRA INFORMATION - TECHNICAL ****
#  NB. LISTS are not totally like java ARRAYS. They do NOT have a fixed limit you have to set at the start! (Don't worry if you don't know about this.)
#  They can dynamically resize, as you append items, they just grow with no problem. As you remove list items, the same can happen with no errors.
#  You can start off with an empty list A = [] . Then go A.append("Hi") and A will now be ['Hi']. That's really painless compared to Java!
#  This is because Python 'Lists' are a more advanced 'Data Structure' than 'Arrays' in other languages --> But that's a more advanced topic!
# ***************************************


# ================== Looping Over Lists ==================
# What if you have a list of items and you want to do something to each item?
# Python is able to do this very quickly and much more easily than Java.
# You simply use a for loop to loop over every item in the list.
# It doesn't matter if the list had 100 items, 3 items or no items, the logic is the same and can be done in one line in Python. 


# ************ Example 10 ************
print("\nExample 10:")

foodList = ['Pizza', 'Burger', 'Fries', 'Pasta', 'Salad'] #Define a list of strings

for food in foodList:
        print(food)
# This loop prints out every item in the list. 
# This is a very powerful tool in Python and shows how you can simply loop through a List.


# ************ Example 11 ************
print("\nExample 11:")
numbers = [1,2,3,4]

for num in numbers:
        print(num)
# Any type of list can be looped over using this construct.
# The above will print out the numbers 1 to 4 - i.e. the entries in list 'numbers'.


# ================== Checking if Something is in a List ==================
# You can simply use an if statement to check if a certain item is in a list.


# ************ Example 12 ************
print("\nExample 12:")
groceryList = ['Bread', 'Milk', 'Butter', 'Cheese', 'Cereal']

if 'Apples' in groceryList:
        print('The item Apples was found in the list groceryList')
else:
        print('The item Apples was not found in the list groceryList')
        
# This is a much quicker way than looping through all the items, such as if you did:
for item in groceryList:
        if item == 'Apples':
                print('The item Apples was found in the list groceryList')



# ================== Using The xrange Function ==================
# The xrange function is a special Python function, that will automatically generate a list of integers within a specified range.

# ************ Example 13 ************
print("\nExample 13:")

num_till_10 = range(0,10)
# This will create a list of integers =[0,1,2,3,4,5,6,7,9] and store it in the variable 'num_till_10'.

num_till_5 = range(0,5) 
# This will create a list of integers =[0,1,2,3,4] and store it in the variable 'num_till_5'.


num_2_till_5 = range(2,5)
# This will create a list of integers =[2,3,4] and store it in the variable 'num_2_till_5'.


# The resulting list can be looped over like any list of integers, e.g., to print the numbers from 1 to 10:
for num in num_till_10:
        print(num)
print("\n")

# Since num_till_10 = xrange(0,10), the above for loop is exactly the same as:
for num in range(0,10):
        print(num)



# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===


# ======================= Play around with Python a bit (Optional Task 1) ============================
#   
#        Create a new Python file in this folder called 'listTypes.py'.
#        Imagine you want to store the names of three of your friends in a list of Strings. 
#        Create a list variable called friends_names, and write the syntax to store the full names of three of your friends.
#        Now write statements to print out the name of the first friend, then the name of the last friend, and finally the length of the list.
#        Now define a list called friends_ages, that stores the age of each of your friends in a corresponding manner.
#        i.e. the first entry of this list is the age of the friend named first in your other list.
#
# ==================================================================================================


# ======================= Play around with Python a bit (Optional Task 2) ============================
#
#        Create a new Python file in this folder called 'loop1000.py'.
#        Imagine I asked you to print out all the numbers from 1 to 1000.
#        Either you'd be up all night writing a list of integers, or you can be smart and use the xrange command.
#        Write 2 lines of code in your file to print out all numbers from 1 to 1000.
#        Once you've got this to work, add logic inside your loop to only print out the numbers from 1 to 1000 that are even (i.e. divisible by 2).
#        Remember the modulo command - i.e., %. 10%5 will give you the remainder of 10 divided by 5. 10 divided by 5 equals 2 with remainder of 0, hence this
#        statement returns 0.
#        Any even number is a number that can be divided by 2 with no remainder.
#
# ==================================================================================================


# ======================= Play around with Python a bit (Optional Task 3) ============================
#        
#        Create a new file in this folder called loopLists.py.
#        Inside it, define a list of Strings of your 5 favourite movies.
#        Now, loop over the list. For each item in the list, print out "Movie: " plus the movies name.
#        Can you figure out how to print out Movie 1: <Movie 1's name>.
#        Movie 2: ... etc?
#        HINT: YOU WILL NEED TO LOOK UP the 'enumerate' command in Python using a Google search.
#        This command allows you to loop over a list retaining both the item at every position, and its index (i.e. position in the list).
#
# ==================================================================================================


# ================= Compulsory Task ==================
# Once you have read and completely understood ​example.py, ​write a Python program that takes in a user input as a String.
# While the String is not “John”, add every String entered to a  list until “John” is entered.
# Then print out the list.
# This program basically stores all incorrectly entered Strings in a list where “John” is the only correct String.
# Save this program as '​John.py' ​in this folder.
# Example program run (what should show up in the Python Console when you run it):
#       Enter your name : <user enters Tim>  
#       Enter your name : <user enters Mark>  
#       Enter your name: <user enters John>  
#       Incorrect names: [‘Tim’, ‘Mark’]


# ================= BONUS Optional Task ==================
# Edit the above program to allow the user to enter an integer before they enter the name.
# This  integer defines how many ‘tries’ the user will get to enter the right name.
# If the user exceeds the number of tries, the program must stop. 




# ******************* CHECKPOINT. Please make sure you understand LISTS, FOR LOOPS, IF STATEMENTS, VARIABLES, and GETTING INPUT ******************************
#  If you do not by this point, then you should go back and try complete the optional tasks above. 
#  If you still feel some things are not clear, please read the attached AdditionalReading.pdf, or login to www.hyperiondev.com/support to get help from your mentor.
# ************************************************************************************************************************************************************

