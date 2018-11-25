# ============ Basics ===================

#A list of Strings:

alphabet = ['a','b','c']

#A list of integers:

numbers = [1, 2, 3]

#A list of doubles:

real_numbers = [1.2, 2.4, 4.9]

#Image the type of data you could store in a list - names, phone numbers, file names, email messages.
#For each of these, think of the variable types that would be used for each list (ie a list of strings or a list of integers or doubles?)

# ============ Reading Lists ===================


#Printing out the first entry in the list called 'alphabet'
print (alphabet[0])

#Printing out all entries in the list
print (alphabet) 

#Printing out the 2nd to last entries of the list
print (alphabet[1:]) #The first entry of a list is at position 0, not 1! That means the 2nd item is at position '1'!

#Looping over all entries in the list called 'alphabet', printing each out

for letter in alphabet:
	print (letter)

for x in alphabet:
	print (x)

#Both of the above loops do the same thing, the variable you define after the keyword 'for' is used to describe the current item of the list within the loop that you do computations with:

for entry in alphabet:
	if entry == 'a':
		print (entry)

#The above loop with loop over all items of the alphabet list, and only print out the item if it is equal to 'a'
