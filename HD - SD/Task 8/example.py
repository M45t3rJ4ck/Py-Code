# Recursion is the process of solving a problem by breaking it up into smaller sub-problems, and solving these. This
# may sound confusing at first, but is an important
# technique, and there are some problems (listed later as additional exercises), which can only be solved by thinking
# recursively! Often, when you are faced with a large task, you accomplish it by breaking the task into smaller, more
# manageable components and then completing
# these in order to complete the overall task.
# Recursion applies this idea to programming.
# Some functional programming languages (like Lisp), do not have looping constructs like "for" and "while",
# but can still accomplish everything that languages like
# Python can by using recursion.
# Here is an example of a recursive algorithm to sum up all consecutive integers from 0 to N. This can easily be
# solved using a loop, but let us consider the recursive
# way:
# Say, we want to work out sum(3), we can break this down into a smaller problem such as 3 + sum(2). The sum of the
# first two integers is easier to work out than the
# first three.
# Similarly, sum(2) = 2 + sum(1)
# Sum(1) = 1 + sum(0)
# And we know that sum(0) = 0
# Since we know that sum(0) = 0, we can easily work out sum(1)
# And since we know that sum(1) = 1, we can work out sum(2)
# And knowing sum(2), we can now work out sum(3), and so on ....
# Analysing this, we obtain sum(3) = 3 + sum(2) = 3 + 2 + sum(1) = 3 + 2 + 1 + 0 = 6 – the desired result!
# So what does the program for this look like?

print("Example 1:")


def sum_num(n):
    if n == 0:
        return 0
    else:
        print("Calculating...", n, "+ sum_num(", (n - 1), ")")
        return n + sum(n - 1)


print(str(sum(3))) 

# The important pattern to note here is that a recursive function will call itself with different parameters every
# time. It must also have one or more “base cases” where it will stop calling itself as the answer is trivial. If
# there is no “base case”, then the calling of functions will never stop and your program will be stuck in an
# “infinite loop” (although there is no iteration here). In this case, the “base case” is when n=0 as the answer must
# be 0.

# ----------------------------------------------------------------------------------------------------
# Optional: What if the base case is set as n = 1? Will the function still work? If so, what changes need to be made?
# ----------------------------------------------------------------------------------------------------
# A more informative version of this recursive function is shown below:

print("Example 2:")


def sum_verbose(n):
    if n == 0:
        print("The sum of n = 0 is 0")
        return 0
    else:
        print("Calculating...", n, "+ sum(", (n-1), ")")
        calc = n + sum_verbose(n-1)
        print("Calculated sum(", n, ") to be", calc)
        return calc


print(sum_verbose(3))

# Run this example to see how the Call Stack works. For example, consider the line return n + sum(n-1)
# when n = 3 (for example). Here sum(3) suspends its own execution and calls sum(2). It will only resume when sum(2)
# has finished. sum(2) in turn, requires sum(1) and sum(0) to have completed execution.

# ----------------------------------------------------------------------------------------------------
# Optional: Which method do you think would be faster – A recursive implementation of sum or an iterative version? Why?
# ----------------------------------------------------------------------------------------------------
# Since recursion is a tricky concept, here is another example which determines the length of a string without using
# Python's built in length function

print("Example 3:")


def string_length(some_string):
    if some_string == "":
        return 0
    else:
        return 1 + string_length(some_string[1:])


print(string_length("length"))

# This is another example how a larger problem (the length of the whole string) is broken down into a smaller
# problem. If we slice the first character off a string, we know that that one character has a length of one,
# and that we only have to work out the length of the remaining string. Our base case is when the input string is
# a null string as we know that this has a length of 0.

# ------------------------------------------------------------------------------------
# For interest:
# The Towers of Hanoi is a famous puzzle which is thought to have originated in Vietnam.
# http://en.wikipedia.org/wiki/Tower_of_Hanoi. It can however, be solved in just a few lines of Python and is shown
# in the attached file, hanoi.py
