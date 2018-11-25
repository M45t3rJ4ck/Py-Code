#************* HELP *****************
#REMEMBER THAT IF YOU NEED SUPPORT ON ANY ASPECT OF YOUR COURSE SIMPLY LOG IN TO www.hyperiondev.com/support TO: 
#START A CHAT WITH YOUR MENTOR, SCHEDULE A CALL OR GET SUPPORT OVER EMAIL.
#************************************* 


# *** IF YOU DID NOT INSTALL NOTEPAD++ AND PYTHON (VERSION 2.7.3 or 2.7.5) ***
# *** PLEASE STOP READING THIS NOW, OPEN THE INSTALLERS FOLDER IN THIS DIRECTORY, 
#     RUN BOTH FILES TO INSTALL NOTEPAD++ AND PYTHON. ***

# Now that you have ensured that you installed Notepad++, 
# PLEASE ENSURE YOU OPEN THIS FILE IN NOTEPAD++ otherwise you will not be able to read it.
# Right click this file --> Edit with Notepad++. Do not use Notepad or any other program to open this file for now.
# Once in Notepad++, click 'View' on the top toolbar and check 'Word Wrap'. 
# Things should be much easier to read now and comments will not go off your screen.

# *** NOTE ON COMMENTS ***
# This is a comment in Python. 
# Comments can be placed anywhere in Python code and the computer ignores them - they are intended to be read by humans. 
# Any line with a # in front of it is a comment.
# Please read all the comments in this example file and all others.



# =========== Welcome to Your Final Task! ===========
# This task will consolidate the knowledge that you've gained across various tasks.
# Now that you know basic Python, we can start talking about some interesting topics!
# Remember take advantage of google and the Python documents in order to get more information. These are a programmer's greatest tool.


# =========== What is Bioinformatics? ===========
# Bioinformatics is a type of science which deals with methods for storing, retrieving and analysing biological data.
# This includes DNA and protein sequences, structures, functions, pathways and genetic interfaces.
# Bioinformatics also deals with algorithms, databases and information systems, web technologies, artificial intelligence and soft computing.
# It also uses information and computation theory, structural biology, software engineering, data mining, image processing and modelling and simulation.
# Finally, bioinformatics makes use of signal processing, discrete mathematics, control and system theory, circuit theory and statistics.


# =========== Sequence Alignment ===========
# In this task we will focus on using Python to solve a problem known as sequence alignment.
# Sequence alignment is a way of arranging the sequences of DNA, RNA, or protein to identify regions of similarity
# that may be a consequence of functional, structural, or evolutionary relationships between the sequences.


# =========== DNA and Nucleotides ===========
# DNA is a chemical structure found in almost every cell and contains the genetic instructions used in the development and functioning of all known living organisms
# DNA is just a String. Yes, just like in programming; DNA is a long chemical string-like structure.
# A portion of DNA can be broken down into sub particles called nucleotides.
# Nucleotides are smaller molecules that when joined up form the complete String of DNA.

# There are only 4 different types of nucleotides in DNA:
#   Adenine which is just represented by an A .
#   Cytosine which is just represented by a C .
#   Guanine which is just represented by a G .
#   Thymine which is just represented by a T .


# ************ Example 1 ************
# An example of a DNA sequence would be:

DNA = "ACGTAGTA"

# Every codon (3 nucleotides) of DNA can be specified by one Amino Acid. 

print("The DNA sequence 'ACG' is a codon")
print("The 'ACG' codon corresponds to the Amino Acid Threonine ")
print("But it's so tedious using a table to look up every Amino Acid. Let's write a quick program to do it for us")

# Bioinformatics is a very exciting and fast paced field that is changing daily.
# Hyperion Development works with the South African Medical Research Council to develop software for new Bioinformatics methods.
# Contact us if you're interested in working on some of these projects. All of these projects involve Python, so we hope you keep working at it!


# ================= Compulsory Task 1 ==================
# Visit the website: http://www.cbs.dtu.dk/courses/27619/codon.html 
# Note the 'SLC' code for each Amino Acid.
# Create a program called SickleCellDisease.py .
# We will simulate the effects of the Single Nucleotide Polymorphism that leads to this genetic disease. 
# Write a function called translate that, when given a DNA sequence of arbitrary length,
# identifies and returns the amino acid sequence of the DNA using the amino acid SLC code found in that table.
#   EG DNA Input: ATTATTATT
#          Output: III
# There are many different amino acids so this may get a bit repetitive. Just do the first five Amino Acids (i.e. I L V F M) and make any other codon be printed as
# the amino acid 'X' 
# So basically, you would use an if - elif - elif .... else structure to translate each codon of DNA into the correct Amino Acid
# Note that the program must be able to handle DNA sequences that are not of a length divisible by 3. 

# Remember: 
#	- len(DNA)  Will return the length of a String
#	- DNA[0:3]  Will get the first 3 characters of the string stored in DNA
#	- num = 3
#	  DNA[0:num]  Will also get the first 3 characters of the string stored in DNA



# ================= Compulsory Task 2 ==================
# Add another function to the program SickleCellDisease.py called 'mutate'.
# This function must read in the contents of the text file named 'DNA.txt'
# It must then identify the first occurrence of the lowercase letter 'a' in 'DNA.txt'.
# You must then write two new text files, one named normalDNA.txt and the other named mutatedDNA.txt.
# The normalDNA.txt must have the same DNA sequence as DNA.txt with the 'a' changed to an 'A'.
# The mutatedDNA.txt must have the same DNA sequence as DNA.txt with the 'a' changed to a 'T'.
# Now create a new function, txtTranslate, that calls the translate function that you wrote in Part 1, to take in text file input.
# Call it on both mutatedDNA.txt and normalDNA.txt, and output both Amino Acid sequences to the user.





