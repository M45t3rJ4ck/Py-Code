# Check if any valid sequence is divisible by M
# Given an array of N integers, using ‘+’ and ‘-‘ between the elements check if there is away to form a sequence of
# numbers which evaluate to a number divisible by M
"""
Examples:
Input : arr = {1, 2, 3, 4, 6}
M = 4
Output : True
There is a valid sequence i. e., (1 - 2 + 3 + 4 + 6), which evaluates to 12 that is divisible by 4
Input : arr = {1, 3, 9}
M = 2
Output : False
There is no sequence which evaluates to a number divisible by M.
"""
# Hint: A simple solution is to recursively consider all possible scenarios, i.e either use a ‘+’ or a ‘-‘ operator
# between the elements and maintain a variable sum which stores the result. If this result is divisible by M, then
# return true, else return false.

import random as rand

# print([i ** 2 for i in range(50) if i % 8 == 0])

u_in = str(input("Please enter a 5 number sequence: \n"))
nums = [int(i) for i in u_in]
r_num = rand.randint(2, 10)
print("Random number: ", r_num)
sum_num = 0
output = False
for num in nums:
    while sum_num % r_num == 0:
        sum_num = sum_num + num or sum_num - num
        output = True
print(str(output))


# print([int(i) for i in u_in if sum_num % r_num == Bool])
