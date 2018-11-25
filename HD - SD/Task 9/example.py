# Welcome to Natural Language Processing, Distributions and Corpuses in Python!
# We can now start talking about interesting topics now that you know basic python.
# There will be fewer optional tasks but feel free to go back to the previous tasksif you've forgotten any of the
# basics! When opening this in Notepad++, please make sure you go to View in the Notepad++ toolbar and make sure the
# 'Word Wrap' option is ticked! NLTK is a rich module for Python that has a whole host of features, developed at the
# University of Edinburgh. It has a list of 'corpuses' built in to it. 'Corpus' is the latin word for 'body'. A
# 'corpus' in NLTK is a body or set of words that form a text. For example, NLTK has the speeches that all US
# presidents gave when they were elected (their inaugural speeches) built into it. Note that there are no optional tasks
# in this section, because familiarizing yourself with the NLTK is important even if you are an experienced programmer.
# Please complete the tasks in the boxes below.


# ======================= 		Learning how to use NLTK - Task 1     ============================
# Write all the Python code below in a new file called corpuses.py and make sure you understand it!
# You must work in your Dropbox folder so we can see your progress.
# Run your file everytime something new is added so you can see how it works.
# There is a compulsory exercise for Task 1 that needs to be completed at the bottom of your corpuses.py

# === Part 1: Importing Corpuses ===
# This statement should work fine if you have NLTK, Numpy and PyYaml installed fine
import nltk
from nltk.corpus import inaugural

# But remember..
# ********* HELP *****************
# REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON STUDENTS@HYPERIONDEV.COM
# Visit www.rmoola.com/advice.html for all the ways you can get free help!
# *************************************

# ---------------------- IMPORTANT ------------------------------------------
#   Please make sure you have read and understand the Instructions file for this task.
#   We will be working with the *Natural Language Toolkit* which is an EXTERNAL Python module.
#   YOU MUST INSTALL IT BEFORE YOU CAN COMPLETE THIS TASK. ALL REQUIRED INSTALLATION FILES ARE GIVEN.
# ---------------------------------------------------------------------------
#   *STEP 1*
#   Open the folder 'Installers' inside this Task 4 folder.
#   There is an exe file in this folder called 'NLTK installer.exe'. Run it and install.
#   If you get an error 'Python cannot be found in the registry' , please email students@hyperiondev.com and we will 
#  email you a file you need to run to fix this error.
#  YOU CANNOT CONTINUE WITH THE OTHER INSTALLATIONS OR THIS TASK IF YOU GET HTIS ERROR.
# ---------------------------------------------------------------------------
#   *STEP 2*
#   After you have installed this NLTK installer, run either the 'Numpy 32 bit windows installer' or 
#   'Numpy 64 bit windows installer' depending on the type of windows you have on your PC.
#   To find out if your computer is running a 32-bit or 64-bit version of Windows in Windows 7 or Windows Vista
#   open System by clicking the Start button , right-clicking Computer, and then clicking Properties.
#   Under System, you can view the system type.
# ---------------------------------------------------------------------------
#   *Step 3*
#   Now run the PyYaml installer.exe file. 
#   Now open the Python Shell (Windows search 'Python' and open 'Python (Command Line)'
#   Inside the black popup box type import nltk and then hit enter.
#   On the next line type nltk.download() and then hit enter.
#   A box called 'NLTK Downloader' will open. Select 'all-corpora' and then click the 'Download' button on the bottom
#   left. This will download the corpuses that you use in Task 1 of this exercise. If you haven't done this properly,
#   you'll get an error when trying to import certain corpuses because they haven't been downloaded to your PC yet. Let
#   us know ASAP if you're having trouble getting the nltk.download() command to work!
#   If your internet connects through a proxy, check out http://nltk.org/data.html on information on how to get
#   nltk.download() command to work through the proxy.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
#   *Step 4*
#   Now run the matplotlib installer.exe file. 
#   Follow the instructions to install. 
# ---------------------------------------------------------------------------
#   *Check*
#   Open your Windows command line (Start->Search 'cmd'->Open)
#   In the black box type 'python' without the quotes and hit enter
#   If this doesn't work, you didn't setup python on the command line correctly and should email us ASAP.
#   Now type 'import nltk'
#   If nothing happens and your cursor goes to the next line - Hooray!
#   If you get any type of error, please make sure you followed the three steps above. 
#   There are *4* seperate installers you should have run - NLTK installer, Numpy installer (either 32bit or 64) PyYaml
#   and matplotlib installer. Please email us ASAP if you can't the 'import nltk' statement to work!
# --------------------- IMPORTANT ------------------------------------------


# ======= Working with the NLTK ===== #

print(inaugural.fileids())

# Run your file.You should see all the text files containing all the speeches of the US presidents that the
# NLTK has saved inside it.
# Now add the lines:

print("=============Words in Obama's Speech ======")
print(inaugural.words('2009-Obama.txt'))  # Returns a list of all the words in Obama's speech
print("=============Words in Bush's speech ======")
print(inaugural.sents('2005-Bush.txt'))  # Returns a list of all the sentences in Bush's speech

# As you can see, the words of Obamas speech are printed in a list, as are the sentences of Bush's speech.
# Try add code to your program to find and outprint the first 25 words of Obama's 2009 speech.

# ===  Part 2: Analysing tokens (words) of a text ===
# The term 'token' means a word or a punctuation mark.
# After you've done that, add the following lines to your program

from nltk.book import * 

# This may take a while to load. NLTK has many texts stored in it!
# Once its loaded type:

print(text1)
print(text6)

# As you can see there are many built in books and even movie scripts that we can come back to to do some processing of
# later.
# Try add:
print(list(text1)[0:100])  # Prints the first 100 words in the Moby Dick book
print(len(text1))  # Find the total number of words in the text
print(len(set(text1)))  # Prints the number of UNIQUE words in the text

# The lexical richness of a text is a count, on average, of how many times each word appears in the text.
# We can get this by diving the total number of TOKENS by the number of unique words ie:

print(len(text1)/len(set(text1)))  # On average, each work in Moby dick occurs 13 times

print(len(text6)/len(set(text6)))  # As a comedic movie, we expect Monty Pyton to be less 'lexically rich' than
# the novel Moby dick and we can see this is true from this statement!

# === Part 3: Analysing frequency of words ===
# NLTK has a built in function that lets us find the frequency of words
# 'Distribution' is a fancy word for what we get if we gather up all the individual frequencies of words and store
# them somewhere. Hence the 'Frequency Distribution' of the words in a text is a sort of table of all the frequencies of
# each word in a text

from nltk import FreqDist
fd = FreqDist(text1)  # We create a frequency distribution of all the words in text1 ie Moby Dick

# Now try:
print(fd['the'])  # Returns the number of times 'the' appears in the text

print(fd.keys()[0:30])  # Prints the first 30 unique words of the text in decreasing order of frequency
print(fd.items()[0:30])  # Does the same as above but also shows the frequency of each word

# === Part 4: Your task ===
# At the end of corupuses.py (you can comment out the above code if its not needed), write python code that:
# 1.) Returns the 10 most frequent words in Obama's 2009 inaugural speech, including their frequencies
# 2.) Calculates the Lexical Richness of his speech
# 3.) Calculate the average length of the sentences in his speech

# === Optional Challenge ===
# 4.) Write a seperate function called sent_length that takes in a string for the name of a text
# 	  like '2009-Obama.txt', then finds the average length of the sentences in that speech.
# 	  Compute the average length of sentences from the year of the first speech (1789) to
# 	  the year of Obama's 2009 speech and see how the average length of sentences has changed
# 	  over the time of the entire US's history. Remember that inaugural.fileids() will
# 	  give you a list of all the String names of the speeches so you don't
# 	  need to work out each name of each speech.
# =================================================================================================


# ======================= 		Learning how to use NLTK - Task 2    ============================
# 	This task is intended to introduce you to slightly more theoretical aspects of Artificial Intelligence.
# 	Your task will include investigation into how humans understand language and what proof we have for this!
# 	The work of a Computer Scientist should never just be about programming..
# 	Create a new python file in this folder called gardenpath.py
# 	In the file type the following code:

sentence = "I made her duck"

# For most kinds of speech processing, we need to identify and classify the words of the text
# by giving them each a part of speech tag.
# Now remember how we briefly talked about 'Part of Speech' tagging in the example 'I made her duck'?
# Remember from school that the different parts of speech are things like verbs (doing words),
# adjectives (descriptions like 'blue'), nouns (things like 'book') and we'll soon discover a lot more.
# Remember that we said 'duck' could either be a noun (the animal with a beak) or a verb (the action to move your
# head down) - ie it has two possible part of speech tags depending on the context.
# Before we can begin to tag each word in the sentence, we must first break up the sentence to get each individual
# word.

listWords = sentence.split()  # Puts each word of the sentence into a seperate block in a list
print(listWords[0])  # Prints 'I'

# This is called TOKENIZATION, and NLTK has a built in method to do this for you.
# The NLTK has a built in POS (Part of speech tagger)
tokens = nltk.word_tokenize("I made her duck")  # Splits up the sentence in words
print(nltk.pos_tag(tokens))  # Tags each word with a part of speech

# Check out how it's tagged the sentence, duck is tagged as VBP - a verb!
# So NLTK has tagged this sentence to mean what we would normally think - you made her move down quickly
# You can find out what any of the tags actually stand for by querying them as follows:

print(nltk.help.upenn_tagset('VBP'))  # Queries what POS tag 'VBP' stands for, explains to you and gives you some
# examples of words with that tag. Note it uses the UPenn (Uni. of Pennsylvania) set of tags which were created when
# they first tagged the first corpus of words by hand

# === Your task ===
#   Let's have some 'fun'.
#   Go to http://en.wikipedia.org/wiki/Garden_path_sentence and have a brief read at what a 'Garden Path sentence' is
#   (at the top) and look at the 'Examples'. Remember that 'parsing' is when we or a computer try tag words given to us
#   to so we can understand what the sentence actually MEANS. Use some Garden Path sentences or think up your own (at
#   least 5). In your file called garden.py that should be working in for this task, tokenize and pos tag each of the
#   sentences after you have stored them in a list called garden path Sentences. See how NLTK has pos tagged these
#   sentences and look up the POS tags you don't understand by using the nltk.help.upenn_tag set command. At the bottom
#   of your file, write a comment about one unusual tag you found that NLTK gave one of the words of your sentences -
#   did you expect this?

# == Optional Challenge ==
#   Go to http://en.wikipedia.org/wiki/Garden_path_sentence#Parsing
#   Read about the different Parsing strategies.
#   Add a comment at the bottom of your program explaining which parsing strategy you think an AI like Siri (the iPhone
#   4 talking robot) uses and why? What kind of datastructures might you suggest is used in this process? Go to
#   http://www.inf.ed.ac.uk/teaching/courses/inf2a/slides/2011_inf2a_L22_slides.pdf and read up till #slide 16 of this
#   University of Edinburgh slide on Human Parsing. How do you think humans eyes respond when encountering a Garden Path
#   sentence and what type of parsing (serial or parallel) do you think this is evidence of?
# =================================================================================================
