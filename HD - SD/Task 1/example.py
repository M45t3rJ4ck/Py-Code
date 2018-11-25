#  This is a comment in python. Comments can be placed anywhere in Python code and the computer ignores them 
# - they are intended to be read by humans. Any line with a #  in front of it is a comment.

#  *** IF YOU DID NOT INSTALL NOTEPAD++ AND PYTHON (VERSION 2.7.3 or 2.7.5) ***
#  *** PLEASE STOP READING THIS NOW, OPEN THE INSTALLERS FOLDER IN THIS DIRECTORY, RUN BOTH FILES TO INSTALL NOTEPAD++ AND PYTHON. ***

#  Now that you have ensured that you installed Notepad++, PLEASE ENSURE YOU OPEN THIS FILE IN NOTEPAD++ otherwise you will not be able to read it.
#  Right click this file --> Edit with Notepad++. Do not use Notepad or any other program to open this file for now.
#  Once in Notepad++, click 'View' on the top toolbar and check 'Word Wrap'. 
#  Things should be much easier to read now and comments will not go off your screen.

#  Please read all the comments in this example file and all others. 

# ========= Welcome to the Hyperion Web Developer Python course ========= 

#  Welcome to the Python programming course for people with no background in programming!
#  This is the start of a course in programming. If you successfully complete the few basic tasks, you'll be learning about exciting topics such as Artificial
#Intelligence.
#  Python is one of the easiest languages to learn how to program. Programming takes patience and practice, and we hope to guide you through this with our course.

# ========= Basic concept of programming ===
#  Programmers write statements of code to create 'programs' - runnable files that do something.
#  Code can be written in different programming LANGUAGES - Python, Java, C are examples of programming languages.
#  This course is a programming course in the Python language. Hyperion has programming courses in other languages such as Java.

#  We write commands, or code in the programming language Python and save these commands in a Python file (.py extension in Windows).
#  You can then 'run' the Python file to make the code execute and the program execute the programs statements to produce an output or other effect determined by the
#statements.
#  Information about how to 'run' Python files are given at the bottom of this file.
#  But first lets get started on how to write some basic code in Python, and perform some basic operations.

# ========= Reading Python code ===

# You're actually reading an example Python program right now.
# Comments in Python appear in GREEN if you have the file opened in Notepad++. Keywords of the Python language appear in BLUE. 
# Python is VERY similar to Java and most programming languages have the same structure so if you learn one - you an learn more easily! It's not like learning human
#languages.
# Almost all programming languages share common SYNTAX, or the way the statements are written.

# ========= Variables ===========
#  A variable is a way to store information. 
#  Variables are created in a part of your computer memory and that area is reserved for the use of the variable in your program while the program runs.

#  Q: How do I use a variable in Python
#  A: Give your variable a name, and give it some information

num = 2
num = 3

#  Q: I see in the line above that there is something called 'num'?
#  A: Yes, that is an example of a variable. The variable num is currently storing the number 2 within itself

#  Q: If I can give a variable information, can I change it?
#  A: Yes, after we set num to be 2, the subsequent line changes the variable num and assigns it a value of 3

#  Q: So can I use a sentence as a variable name?
#  A:  Not really, there are restrictions on variables in terms of naming so you have to comply, know that letters and underscores are permitted and anything else
#should be avoided
#       Below is an example of bad naming convention vs good

myName = "Tom"
variableOne = "Tom"
string_name = "Tom"
h4x0r = "Tom"

#  myName and string_name are examples of descriptive variables as they reveal what their functions are and what content they stored
#  variableOne and h4x0r are terrible names and are not descriptive. 

#  Remember that you can name variables as you please, but don't make it hard on yourself


# ======================= Play around with Python a bit  ============================
# 
# 	At this point, why not play around with creating variables? Press the windows Start button (in the bottom left corner of your screen), in the 'Search for
#programs and files' box, 
# 	type 'Python (command line)' and you should see a program named exactly that pop up. Click to run the program.
# 	In the black box that appeared, type: 
# 	
# 	name = "John"  
# 
# 	then press enter. Nothing happens but this Python program has remembered what you set the variable 'name' to.
# 	To prove this type: 
# 
# 	print name 
# 
# 	and then hit enter. 'John' should be printed out by the program. 
# 	If you close this black box, and open a new one and type: print name , you will get an error. This is because you were coding Python 'Shell' and your
#variables aren't saved. 
# 	We write Python in text editors like Notepad++ or the IDLE Python GUI so that all our variable definitions and code are saved. We can then run these files
#as python programs at any time we want, and we can use these 
# 	programs repeatedly. Keep the black box open and try out some commands as you read through this file. Try to add some numbers and variables as shown below.
# 	 -> you are actually writing Python already, it's that simple!
# 
# ==================================================================================================


# ========= Data types ===========

#  Q: Are variables specific in what they store?
#  A: Their content is specific. The content a variable stores is the data and the type of data is intuitively called the data-type.
#      There are different types of data, there are Integers, Floats and Strings to mention a few.
#      Integers store whole numbers and are also known as ints. Floats store decimal numbers and are sometimes called doubles. Strings store text (which is a fancy
#character array)

#  Q: Do we have to declare the data-type of a variable?
#  A: No, the data-type can be neglected when creating a variable. This is known as 'weak-typing'

a_string_variable = "ABC"
an_int_variable = 2

#  Q: How does Python know the difference between variables?
#  A: Python detects the type of a variable by reading how it is given to the variable and the extra information with it.
#      Strings are detected with quotation marks " "
#      Integers are detected with the lack of quotation marks and being digits or another accepted number format
#      Floats are detected with a decimal point
#      Take heed that types can be converted from one to another, but you need to take care when setting a string with numerical information for example and your
#intention thereof.

text = "Welcome" 
number = 10 
numberStr = "10" 

# Watch out! Since you defined 10 within quotation marks, Python knows this is a String. It's not an integer even though we understand 10 is a number

# When writing programs, you'll have to decide what data types or variables you will need to do what you want your program to do.
# In most cases, it will be pretty obvious - want to store someone's name? Use a String. Their age? Use an integer. 

# ========= Arithmetic Operations ===========
#  Q: What are we allowed to do with variables and arithmetic operations?
#  A:  We can do all the basic operations like addition, subtraction, multiplication and division with symbols +, -, * and / respectively

#  Q: Can I add a number and a variable storing a number together?
#  A: Yes, remember that the number will be read by Python from the variable and it will act as a number.  Same thing as in mathematics as with those variables.
#      Remember that a variable represents what it stores.

# Addition operations:

number = 2+5	#  a result of 7 is stored in number
number = number - 5 #  number now stores a value of 2

#  We can also use existing variables to create new ones

four = 4
two = 2

answerAdd = four + two 
answerSubtract = four - two

#  answerAdd has a value of 6 (because 4 + 2 = 6)
#  answerSubtract has a value of 2 (because 4 - 2 = 2)

#  Multiplication and division

answerDivide = four/two		
answerMultiply = four*two	
#  answerDivide has a value of 4/2 (2)
#  answerMultiply has a value of 4*2 (8)
# Can you see how these statements could be used to create a calculator or even a simple program to do some kind of mathematics?
# We can even use variables to store a new value from themselves as follows:

numDouble = 2 						
numDouble = numDouble * 2	
#  numDouble stores 2
#  numDouble stores 2*2 = 4

#  Be careful! You can only perform certain arithmetic operations on variables of the same data type.
#  EG: You can add two variables if they are both integers and the result will also be an integer as expected.

# ========= Operations on different Data Types ===========
#  If you add string objects they will be CONCATENATED (put side by side or join). You cannot subtract or divide String variables - that's only for ints or Floats. 

firstName = "Phil"
lastName = " Jones"

fullName = firstName + lastName 

# the variable fullName now stores the string "PhilJones" , we have concatenated the two strings
# You can use the multiplication operator on a string to duplicate a string n times

firstNameDuplicatedSevenTimes = firstName * 7 

#  Results in "PhilPhilPhilPhilPhilPhilPhil"
# You can concatenate as many strings as you want in a statement, as long as they are all of the same string data-type.

sentence = "Hello my name is : " + fullName         

#  We concatenated the String "Hello my name is: " (which isn't stored in a variable) to the contents of the String variable fullName. 
#  "Hello my name is : " is an example of a literal or constant
#  We'll discuss how to concatenate/add variables of different data-types later.


#  =========== Running Python files =====================

#  Now that you know how to write code, it's time to learn how to execute your code to see what the output is.
#  Remember you're actually reading a Python file now. All the Python commands are the statements not seen in GREEN.
#  Let's 'RUN' this Python file and take a look at what output it produces (if any).
#  When you write Python code, you'll have to run it often to test that your programs are doing what you'd like them to do.

# There are three different ways to 'run' Python files.

#  ======== OPTION 1: Run from IDLE Python GUI -- THE EASY WAY ========
# The easiest way to run Python files and this program is through a GUI (Graphical User Interface). 
# Please follow these steps to run this program:

# Simply go to the Windows Start Button at the bottom left corner of your screen and enter 'IDLE' into your windows search ('Search for programs and files' box).
# The program 'IDLE (Python GUI)' should appear in the search box. Click it to open it.
# If you can't find the IDLE program on your computer - you didn't install Python correctly. Contact us for assistance.
# Go to the top left corner of this program (it looks like a white box when open) and click --> File -- Open--> navigate to your Dropbox folder and open example.py.

# You can find your example.py file under C:/Users/<Your User Name>/Dropbox/<Your surname and first letter>/Task 1/example.py

# Now your code will open in the Python GUI IDLE. Press F5 on your keyboard to RUN the Python and the output will appear in a separate python output (Python Shell)
#window!
# You can use this method to run ANY python file (file with a .py extension). 
# If there is an error in your code, the code won't run and the error will be printed out in the Python Shell windows.
# Another way to run Python files is to simply right click on this file (example.py) and select 'Open in IDLE'. You may or may not see this option.

# Errors are things like trying to add two variables that aren't the same data type, or using a variable that isn't declared! 
# (ie if you say num = num1+num2 and you haven't said what num1 and num2 above this statement!)
# We'll talk about errors more later.

# Let's put a line just below this comment that will print out the words 'Yay! You ran your first Python program!' when the file example1.py is run using IDLE.

print ("Yay! You ran your first Python program!")

# Now when you follow the instructions above and open example1.py in the IDLE program and hit F5. 
# You should see "Yay! You ran your first Python program!" printed out in the Python Shell window!
# Whatever appears in the Shell window after running a program is known as the OUTPUT of a program.
# All the code above that aren't comments also ran, but just storing and declaring variables doesn't produce any output. 
# The Python Shell only shows the output of the program.

# I advise that you complete all tasks and open all example files in IDLE from now on.
# Perhaps create a shortcut to IDLE on your Desktop so that you can access it faster.
# Notepad++ can only be used to view the text of a code - you can't run the program from within Notepad++ unfortunately.


# ======================= Play around with Python a bit  ============================
# 
# 	Now that you know how to run Python files, it is helpful to look at some example Python code.
# 	Inside this Task 1 folder, there is a folder called 'Example programs'.
# 	There are several example programs inside this folder.
# 	Open each file using IDLE in the method explained above.
# 	Take a look at the code to get a better idea of some of the concepts discussed above.
# 	Run each file to see the output of each program. (the exampleErrors.py file won't run, don't worry about that.)
# 
# ==================================================================================================

# The other two options are OPTIONAL. As long as you know how to use IDLE, you can complete our entire course.

#  =========== Option 2: Use any GUI/IDE that you want.  -- ADVANCED ===========
# An IDE is a program like the IDLE Python GUI.
# You get many programs that let you run code within them.
# Some of these IDEs are more complicated than others.
# See http://wiki.python.org/moin/PythonEditors for a huge list of your options of different IDE's that you can run Python files from.

# =========== OPTION 3: Run from the windows command line (cmd)  -- THE HARD WAY =========== 
# Once you have set up Python to work from your command line, open cmd (Start --> search for cmd -> open cmd), then navigate to this directory by typing the commands
#into the black box:
# 
# cd Dropbox
# cd <this folder name -> should be your firstname and first initial of surname eg RiazM) 
# cd Task 1
# python example.py
# This program should now run from your command line. If this does not work, Python is not set up correctly on your command line.
# You can contact your trainer

# ==========================================================

# Play around with this program in IDLE. Change statements and delete things, run the code and see what happens.
# Additional examples of basic python can be found in AdditionalReading.pdf but you are not required to read the entire thing.

#  There is an example2.py file within this folder, open it and read the contents
#  If you having any issues, let us know. We don't bite :)




