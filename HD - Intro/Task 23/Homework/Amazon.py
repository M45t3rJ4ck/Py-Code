# Create a Python file called "amazon.py" in this folder.
# Write code to read the content of the text file input.txt.
# For each line in input.txt, write a new line in the new text file output.txt that computes the answer to some operation on a list of numbers.
# If the input.txt has the following:
#       Min: 1,2,3,5,6
#       Max: 1,2,3,5,6
#       Avg: 1,2,3,5,6
# Your program should generate output.txt as follows:
#       The min of [1, 2, 3, 5, 6] is 1.
#       The max of [1, 2, 3, 5, 6] is 6.
#       The avg of [1, 2, 3, 5, 6] is 3.4.
# Assume that the only operations given in the input file are min, max and avg, and that the operation is always followed by a list of comma separated integers.
# You should define the functions min, max and avg that take in a list of integers and return the min, max or avg of the list.
# Your program should handle any combination of operations and any length of input numbers.
# You can assume that the list of input numbers are always valid integers and that the list is never empty.

import math
import os
input_file = open("Input.txt", "r")
nums = input_file.readline()
print(nums)
maximum = max(nums)
minimum = min(nums)
average = (len(nums) / sum(nums))
output_file.write(" The min of " + str(nums) + " is " + str(maximum) + ". \n")
output_file.write(" The max of " + str(nums) + " is " + str(minimum) + ". \n")
output_file.write(" The avg of " + str(nums) + " is " + str(average) + ". \n")
