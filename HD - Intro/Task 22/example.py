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


# =========== Python List Methods  ===========
# There are many useful built-in List methods available for you to use.
# We have already looked at the 'append()' method.
# Some other List methods can be found below:
#   extend()    - Adds all elements of a list to the another list
#   insert()    - Inserts an item at the defined index
#   remove()    - Removes an item from the list
#   pop()       - Removes and returns an element at the given index
#   index()     - Returns the index of the first matched item
#   count()     - Returns the count of number of items passed as an argument
#   sort()      - Sorts items in a list in ascending order
#   reverse()   - Reverses the order of items in the list


# =========== The copy Module  ===========
# Lets take a closer look at the copy module.
# There are several ways to make a copy of a list.
# The simplest way to make a copy is to use the copy() method.
# Using the copy() method ensures that if you modify the copied List, the original List remains the same.
# However, if your List contains other Lists as items, those inner Lists in the original List can still be modified
# if, the corresponding inner List in the copied List is modified.
# This is called a shallow copy.
# Slicing Lists also creates a shallow copy of a List.
# Therefore, when the List contains other Lists as items, the inner Lists have to be copied as well.
# You could do this manually but Python already contains a method to do it, the deepcopy() method.
# In order to use the deepcopy() and copy() methods you must import the copy module.


# ************ Example 1 ************
print("Example 1:")
import copy

a = [[1, 2, 3], [4, 5, 6]]
b = copy.copy(a)
c = a[:]
d = copy.deepcopy(a)

b[1][0] = 10
c[1][1] = 11
d[1][2] = 12

print("List a: ")
print(a)
print("List b: ")
print(b)
print("List c: ")
print(c)
print("List d: ")
print(d)



# =========== List Comprehension  ===========
# List comprehension can be used to construct lists in an elegant and concise way.
# It is a powerful tool that will apply some operation to every element in a list, and then put the element into a new list.
# List comprehension consists of an expression followed by a for statement inside square brackets.

# ************ Example 2 ************
print("\nExample 2:")

numList = ['1', '5', '8', '14', '25', '31']
print(numList)

newNumListInts = [int(element) for element in numList]
# We are looping over numList, which is a List of Strings 
# For each element, we are casting it to an Integer and putting it into a new list, newNumListInts.

print(newNumListInts)  # Do you see the difference?

# We can now sum this list, since newNumListInts is a list of integers and not Strings.
print(sum(newNumListInts))
# We can compute the sum of the Integers using the built-in function sum()
# This function gives you 1+5+8+14+25+31=84.


# ************ Example 3 ************
# You can do many operations with list comprehensions. 
print("\nExample 3:")

doubleList = [2 * element for element in newNumListInts]
# A new list, with each element double its value in the previous list.
print doubleList


halfList = [0.5 * element for element in newNumListInts]
# A new list, with each element half its value in the previous list.
print(halfList)


# =========== Dictionaries ===========
# Dictionaries are used to store data and are very similar to Lists.
# However, Lists are ordered sets of elements, whereas dictionaries are unordered sets.
# Also, elements in dictionaries are accessed via keys and not via their positions like how lists are.
# When the key is known, you can use it to retrieve the value associated with it.


# =========== Creating a Dictionary ===========
# To create a dictionary simply place the items inside curly braces and separate them by commas.
# An item has a key and a value, which is expressed as a pair (key: value)
# Items in a dictionary can have a value of any datatype, however the key must be either a String or number and must be unique.

# ************ Example 4 ************

# An empty dictionary 
empty_dict = {}

# A dictionary with integer keys
int_key_dict = {1: 'apple',
                2: 'banana',
                3: 'orange'
               }

# A dictionary with string keys
string_key_dict = {'name': 'John',
                   'surname': 'Doe',
                   'gender': 'male'
                  }

# A dictionary with mixed keys 
mix_key_dict = {'word': 'Python',
                2: [1, 3, 4, 5]
               }


# =========== Accessing Elements from a Dictionary ===========
# While you might use indexing to access elements in a list, dictionaries use keys.
# Keys can be used to access values either by placing them inside square brackets [], such as with indices in lists, or with the get() method.
# However, if you use the get() method, it will return 'None' instead of 'KeyError', if the key is not found.

# ************ Example 5 ************
print("\nExample 5:")

profile_dict = {'name': 'Chris',
                'surname': 'Smith',
                'age': 28,
                'cell': '083 233 3242'
               }

# Using square brackets []
print(profile_dict['surname'])
# prints out 'Smith'

# Using the get() method
print(profile_dict.get('cell'))
# prints out '083 233 3242'


# =========== Changing Elements in a Dictionary ===========
# We can add new items or change items using the assignment operator (=)
# If there is already a key present, the value get updated, else if there is no key a new key: value pair is added.

# ************ Example 6 ************
print("\nExample 6:")

profile_dict = {'name': 'Chris',
                'surname': 'Smith',
                'age': 28,
                'cell': '083 233 3242'
               }

# Changing a value
profile_dict['age'] = 29
print(profile_dict)

# Adding a value
profile_dict['gender'] = 'male'
print(profile_dict)

# =========== Dictionary Membership Test ===========
# You can test if a key is in a dictionary by using the keyword 'in'.
# You simply enter the key you want to test for membership, followed by the 'in' keyword and lastly the name of the dictionary.
# This will return either True or False, depending on whether the dictionary contains the key or not.
# The membership test is for keys only, not for values.


# ************ Example 7 ************
print("Example 7:")

doubles = { 1: 2,
            2: 4,
            3: 6,
            4: 8,
            5: 10
          }

print(1 in doubles)
# prints out True

print(8 in doubles)
# prints out False



# ************ Example 7 ************
# Imagine we have a long list of codewords and each codeword triggers a specific function to be called.
# For example, we have the codewords 'go' which when seen calls the function handleGo, and another codeword 'ok' which when seen calls the function handleOk.
# We can use a dictionary to encode this.

def handleGo(x):
    return "Handling a go! " + x


def handleOk(x):
    return "Handling an ok!" + x


# This is dictionary:        
codewords = { 
  'go': handleGo,   # The KEY here is 'go' and the VALUE it maps to is handleGo (Which is a function!).
  'ok': handleOk,   
}
# This dictionary pairs STRINGS (codewords) to FUNCTIONS.


# Now, we see a codeword given to us:
codeword = "go"


# We can handle it as follows:
if codeword in codewords:
        answer = codewords[codeword]("Argument")
        print(answer)
else:
        print("I don't know that codeword.")

        

# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===



# ================= Compulsory Task 1 ==================
# Create a new Python file in this folder called cafe.py.
# Create a list called menu, which should contain at least 4 items in the cafe.
# Next, create a dictionary called stock, which should contain the stock value for each item on your menu.
# Create another dictionary called price, which should contain the prices for each item on your menu.
# Next, create a function which will calculate the total stock worth in the cafe. You will need to remember to loop through the appropriate dictionaries and lists to do this.
# Finally, print out the result of your function.


# ================= Compulsory Task 2 ==================
# Create a new Python file in this folder called hash.py
# Create a dictionary called countryMap, where the the KEYS are the name of a country (i.e. a String), and the VALUE for each key is the name of that country's capital city.
# For Example:
#    countryMap = {
#        'UnitedKingdom': 'London',
#        'Sweden': 'Stockholm',
#        'Canada': 'Ottawa',
#    }
#    What does print countryMap['Sweden'] return?


# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Write a program that is able to give you the meaning of a given abbreviation.
# Create a dictionary that contains some abbreviations and their meanings.
# Let the abbreviation be the key and the meaning of the abbreviation be the value (e.g. ADSL: Asymmetric Digital Subscriber Line).
# Make sure that you dictionary has at least 4 abbreviations and their meanings.
# If you need ideas on some abbreviations, go to http://www.abbreviations.com/
# After you have created your dictionary add 2 more abbreviations and their meanings to it.
# Now ask the user to enter an abbreviation and check if that abbreviation is in your dictionary.
# If it is print out the abbreviation and it's meaning.
# If it is not in the dictionary, print out "Abbreviation not found"
