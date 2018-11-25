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


# ========= User-Defined Functions  ===========
# There are times when programmers find that they often have to execute the same piece of code again.
# For example, just say you wrote several lines of code that, given a filename, can open the file, read its contents and print out its contents to the screen.
# It may be useful to 'save' that code somewhere so you could easily reuse it.
# A programmer can define a function, named something like 'read_file', that would encode this logic.
# That way, the next time they need to read the contents of a file they simply 'call'(use) the function 'read_file'.
# This will 'return' the result of that function, which in this case is the output to be printed to the screen.


# ========= How to Define a Function ===========
# Defining a function simply means creating a function.
# You begin with the keyword def followed by the name of the function and parentheses, ().
# You place any input parameters (values passed to the function) within these parentheses.
# You then place a colon (:) after the the parenthese to signify the start of the indented code block.
# The indented code block contains statements that provide the functionality to your function.
# The last statement in the indented code block is the return statement.
# This statement exits the function and can also pass a value back to the caller.

# The general syntax of a function in Python is as follows:
# def functionName(parameters):
#       statements
#       return (expression)


# ************ Example 1 ************

def addone(x):
    y = x + 1
    return y

# Explanation:
# This function is called 'addone', it takes as input the parameter 'x'.
# We can call the input variable (here x) anything we want.
# It's just a name we give it so we know how to refer to it within the function (every indented line under the def addone(x) line is 'within' the function).
# The code indented under 'def addone' is the logic of the function. It defines what happens when the function is called.
# Simply put, the function computes a new variable y, which is the value stored in variable x with 1 added to it.
# It then 'returns' the value y. 

# Note the 'def' keyword.
# Python knows you're defining a function when you put this in front of a word.
# It will expect a function name, its input parameters, and then a colon, with the logic of the function indented underneath.
# Note the 'return' keyword.
# Python will expect this at the end of your function, but it doesn't always have to be there. More on this later.


# ========= Calling a Function ===========
# In order to execute a function, you need to 'call' it.
# You call a function by using the functions name followed by the values you would like to pass into it within parentheses.

# ************ Example 2 ************
# If you 'called' the function we previously defined with the value of x = 10, it would look exactly like this:

print("Example 2: ")
num = 10
print("10 plus 1 is equal to: " + str(addone(num))+".")
# This will call the function addone defined above and pass the integer 10 to it
# The function will then return 11 and it will be printed out.

# ************ Example 3 ************
# You can also call a function and store the value returned by it in a variable.

print("\nExample 3: ")
num = addone(4)
print("4 plus 1 is equal to: " + str(num) + ".")


# Think of the 'call to the function', i.e. addone(num) , as a 'placeholder' for some computation.
# The function will go off and run its code, and return its result in that place.


# ========= Function Parameters ===========
# In the function definition, you put the names of variables that you what to store the input values to, between the parentheses after the function name.
# You can put more than one of these variables or parameters, simply separate them by commas.
# When you call a function, you place the value you would like to pass to the function in parentheses after the function name.
# This value is passed to the function and stored in the corresponding function parameter variable. 
# When calling a function, be sure to place the values you are passing to the function in the same order as the corresponding function parameters in the function
# definition.

# ************ Example 4 ************
print("\nExample 4: ")
def power(base, exponent):  
    result = base**exponent
    return (result)


print(power(3,5))
        
# Here we've created a function which accepts two arguments and returns the result of the base to the power exponent using the ** operation (where x ** y means x^y).
# Note the order of the values in the calling statement.
# 3 is passed to the variable base while 5 is passed to the variable exponent.


# =========== Where Do Functions Go? ===========
# A major switch has happened when we introduced functions. Before, all your programs were sequential.
# This means that whatever code was written in a file, executed from the top of the file to the bottom.
# With functions, we lose this.
# You can define a function anywhere in your file, BUT IT WILL NOT RUN UNLESS 'CALLED' SOMEWHERE IN THE CODE.
# For example, though we have defined the function 'addone' above.
# The code indented underneath it would never be executed unless there was another line that 'called' addone
# with the command addone(some_variable) SOMEWHERE IN THE MAIN BODY OF YOUR CODE.
# In the next task, you'll explore Object Oriented Programming that will explain these concepts further.



# ************ Example 4 ************
def double_this_number(number):
        y = number*2 # Multiples the number by 2.
        return y


# ************ Example 5 ************
def return_first_letter_word(word):
        y = word[0]
        return y

# ************ Example 6 ************
def put_number_in_list(num):
        newList = []
        newList.append(num)
        return newList

# ************ Example 7 ************
def put_number_in_list_if_big(num):
        newList = []
        if num >100:
                newList.append(num)
        return newList # Be careful! This could return an empty list.

# ************ Example 8 ************
def compute_sum_of_two_numbers(num1,num2):
        y = num1+num2
        return y

# ************ Example 9 ************
def takes_no_parameters():
        y = "This function takes no parameters as input, but that means its functionality is limited...."
        return


# As you can see from the examples above, you can pretty much do anything you want in a function.
# You can create new data structures, use conditionals etc.
# We can call the input variable anything we want. It's just a name we give it so we know how to refer to it within the function. 
# As seen in the second to last example, we can have multiple input parameters too. There's no limit on them, as long as you can keep track of what's what!
# In the last example, we have a function that takes no input parameters. This is also possible, but it means the user who calls the function has limited interaction
# with the function - they can't supply any input!
# In the case of some functions - imagine a function that returned the current time i.e. - getTime() - it makes sense to see why they need no input parameters
# (unless you had a more complex function like get_time(timezone) which returned the time for a specific timezone the calling user provides!)
# Values passed into the function through the 'function's parameters' (variables e.g. num1 and num2 above) will be referenced with those variable names.
# Think of it as copying in the values from the inputted parameter values when 'calling' the function to these 'function parameters'.


# While the above functions may not seem useful, this is because they are so simple. You can have functions with hundreds of lines that do complex tasks.
# However it is often very useful to define functions that do one specific task with a few lines of codes as opposed to a complicated function that does many tasks
# with hundreds of lines of code.
# i.e. break up a complicated function into many simpler functions so that it is easier to understand the function's role and find errors!




# =========== Functions Without Return Statements =========== 
# Functions do not need to have a return statement 

# ************ Example 10 ************
print("\nExample 10:")
def print_word(word):
        print(word)


# The function above just prints out something, it doesn't have a return statement.
# That's okay, but it means that if you make a call like:

y  = print_word("abc")


# y will store the special value None.
# This is not a String or any other data type, so it will cause an error when trying to do other things with it.
# Be careful that your functions return values, if that's what you need them to do.


# ************ Example 11 ************
print("\nExample 11:")
# We can call the function multiple times in a loop:

num = 10
for i in range(10):
    num = addone(num)  #Runs 10 times, each time, 1 is added to the value of 10. So after the first iteration it will be 11, the second iteration computes 11 + 1 = 12,
                       # etc... until 20.
        
print(num)

# ======================= Play around with Python a bit ============================
#
#   Create a new Python file in this folder called funcpractice.py.
#   Inside it, create a function called 'addthree', that takes as input three parameters - num1, num2, num3.
#   Then, write logic to create a new variable, y, that is the sum of all three of these numbers.
#   Then, return the result y.
#   Now, after you've defined this function, write a function call to return the sum of the numbers 52, 25, and 1403.
#   Store this result in a variable called sumFunc.
#   Print out sumFunc. Don't forget to cast to a String!
#
# ==================================================================================================



# ****************** END OF EXAMPLE CODE ********************* # 


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===


# ================= Compulsory Task 1 ==================
# Create a Python file called “myFunction.py” in this folder.
# Create your own function that prints all the days of the week
# Create your own function that takes in a sentence and replaces every second word with the word “Hello”


# ================= Compulsory Task 2 ==================
# Create a Python file called “holiday.py” in this folder.
# You will need to to create four functions:
#   - Hotel cost - This function will take the number of nights as an argument and return a total cost (You can choose the price per a night)
#   - Plane cost - This function will take the city you are flying to as an argument and return a cost for the flight (Hint: use if/else if statements in the function to retrieve a price based on the chosen city)
#   - Car rental - This function will take the number of days  as an argument and return the total cost.
#   - Holiday cost - This function will take three arguments, number of nights, city, and days.
#     Using these three arguments, you can call all three of the above functions with respective arguments and finally return a total cost for your holiday.
# Print out the value of your Holiday function to see the result!
# Try using your app with different combinations to show it’s compatibility with different options



# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Write a program that will act as a calculator.
# Create functions named addNum, subtractNum, multiplyNum and divideNum that asks the user to enter 2 numbers and adds, subtracts, multiplies or divides them respectively.
# Print out the following menu and ask the user to input a number that corresponds to the option they would like to choose:
#       Option 1 - add
#       Option 2 - subtract
#       Option 3 - multiply
#       Option 4 - divide
# If the user enters 1 call the addNum function
# If the user enters 2 call the subtractNum function
# If the user enters 3 call the multiplyNum function
# If the user enters 4 call the divideNum function
# Make sure that the result of the caluation is printed out to the screen.




