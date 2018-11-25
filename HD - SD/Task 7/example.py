# Welcome to Bioinformatics in Python!
# We can now start talking about interesting topics now that you know basic python.
# There will be fewer optional tasks but feel free to go back to Task 1/2 if you've forgotten any of the basics!
# But remember..
# ********* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
# Visit www.rmoola.com/advice.html for all the ways you can get free help!
# *************************************
# ===== Python for Bioinformatics =====
# First off, remember DNA is built up of nucleotides which are either A, C, G or T.
# An example of a DNA sequence would be:

DNA = "ACGTAGTA"


# Recall that every codon (3 nucleotides) of DNA can be specified by one Amino Acid.

print("The DNA sequence 'ACG' is a condon")
print("The 'ACG' codon corresponds to the Amino Acid Threonine ")
print("But it's so tedious using a table to look up every Amino Acid. Let's write a quick program to do it for us")


# ================================ Part 1 of Compulsory Task ===========================
# Visit the website: http://www.cbs.dtu.dk/courses/27619/codon.html
# Note the 'SLC' code for each Amino Acid.
# Create a program called SickleCellDisease.py . We will simulate the effects of the Single Nucleotide Polymorphism
# that leads to this genetic disease.
# Write a function called translate that when given a DNA sequence of arbitrary length, the program identifies returns
#  the amino acid sequence of the DNA using the amino acid SLC code found in that table.
# EG DNA input: ATTATTATT Output: III
# There are many different amino acids so this may get a bit repetitive. Just do the first five Amino Acids
# (ie I L V F M) and make any other condon be printed as the amino acid 'X' 
# So basically, you would use an if - elif - elif .... else structure to translate each codon of DNA into the
# correct Amino Acid
# Note that the program must be able to handle DNA sequences that are not of a length divisible by 3.
# Remember:
len(DNA)  # Will return the length of a String
DNA[0:3]  # Will get the first 3 characters of the string stored in DNA
num = 3
DNA[0:num]  # This will work too!
# If you need a HINT about how to do this, please email students@hyperiondev.com


# ================================ Part 2 of Compulsory Task ===========================
# Add another function to the program SickleCellDisease.py called 'mutate'.
# This function must read in the contents of the text file named 'DNA.txt'
# It must then identify the first occurrence of the lowercase letter 'a' in 'DNA.txt'.
# You must then write two new text files, one named normalDNA.txt and the other named mutatedDNA.txt.
# The normalDNA.txt must have the same DNA sequence as DNA.txt with the 'a' changed to an 'A'.
# The mutatedDNA.txt must have the same DNA sequence as DNA.txt with the 'a' changed to a 'T'.
# Now create a new function, txtTranslate, that calls the translate function that you wrote in Part 1, to take in
# text file input.
# Call it on both mutatedDNA.txt and normalDNA.txt, and output both Amino Acid sequences to the user.

# ================================ Part 3 of Compulsory Task ===========================
# Create a new program called AminoAlign.py with a function named align
# This function must take in any two amino acid sequences , and find all characters in which they differ.
# Run this function on the output of Part 2 (The AA of the mutatedDNA.txt file vs the AA of the normalDNA.txt file)
# and identify the mutated amino acid.
# Remember
print("a" == "b")  # You can compare strings like this

# === Optional Challenge ==
# The strings must be formatted in such a way:
# AA Sequence 1: ILLVFMCAAGPT
# AA Sequence 2: ILLCFMCAAGPS
#               ***_*******_ 
# Alignment: 83%
# Where there is a match in amino acids, a * should be printed beneath the pair. Where there isn't a match,
# a '_' should be printed beneath the pair.
# The percentage of aligned (matching) characters should also be out printed.
# **********In bioinformatics, the alignment % of the DNA of two different animals can tell us how closely
# related they are to each other. More closely related animals with a higher alignment share common
# physical features. *****************
# You should now have a program named SickleCellDisease.py that has functions mutate, translate and txtTranslate
# And a program called AminoAlign.py with the function align.
# =============================================================================================
# Bioinformatics is a very exciting and fast paced field that is changing daily.
# Hyperion Development works with the South African Medical Research Council to develop software for new
# Bioinformatics methods. Contact us if you're interested in working on some of these projects. All of these projects
#  involve Python , so we hope you keep working at it!
# We will come back to Bioinformatics later when you've learnt more about advanced functions in Python.




