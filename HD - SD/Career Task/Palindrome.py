# Arrays & String manipulation
# Given a string, calculate and print all its possible palindromic partitions. (A palindrome is a word, phrase,
# or sequence that reads the same backwards as forwards)
# Examples:
# Input: nitin
# Output: n i t i n
# Input: geeks
# Output: g e e k s
# Hint : Go through every substring of the given string starting from first character, check if it is a palindrome.
# If yes, then add the substring to the solution/display and traverse through remaining part. The use of recursion is
#  handy for this kind of a problem!

U_palin = list(input("Please enter your word for evaluation: \n"))
palin_U = U_palin[::-1]
if U_palin == palin_U:
    print(str(U_palin) + "\n" + str(palin_U) + "\nYou're word is a palindrome!")
else:
    print(str(U_palin) + "\n" + str(palin_U) + "\nYou're word isn't a palindrome!")
