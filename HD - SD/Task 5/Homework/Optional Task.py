'''
    <BONUS Optional Challenge>

    Change your program to also handle the operation 'px' where x is a number from 10 to 90 and defines the x percentile of the list of numbers. For example:

    input.txt:

    min: 1,2,3,5,6
    max: 1,2,3,5,6
    avg: 1,2,3,5,6
    p90: 1,2,3,4,5,6,7,8,9,10
    sum: 1,2,3,5,6
    min: 1,5,6,14,24
    max: 2,3,9
    p70: 1,2,3

    Your output.txt should read:

    The min of [1, 2, 3, 5, 6] is 1
    The max of [1, 2, 3, 5, 6] is 6
    The avg of [1, 2, 3, 5, 6] is 3.4
    The 90th percentile of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is 9
    The sum of [1, 2, 3, 5, 6] is 17
    The min of [1, 5, 6, 14, 24] is 1
    The max of [2, 3, 9] is 9
    The 70th percentile of [1, 2, 3] is 2

'''
import re
from functools import reduce

input_file = open("Input.txt", "r")
output_file = open("Output.txt", "w")
nums = input_file.readline()

regex = re.compile(r"(?<=\w:)*\d")
nums = re.findall(regex, nums)
Snums = [float(i) for i in nums]
Snums = reduce(lambda x, y: x + y, Snums)
for x in range(10, 90):
    px = x % Snums

maximum = max(nums)
minimum = min(nums)
average = (Snums / len(nums))

output_file.write(" The max of " + str(nums) + " is " + str(maximum) + ". \n")
output_file.write(" The min of " + str(nums) + " is " + str(minimum) + ". \n")
output_file.write(" The avg of " + str(nums) + " is " + str(average) + ". \n")
output_file.write(" The p" + str(x) + " of " + str(nums) + " is " + str(px) + ". \n")

input_file.close()
output_file.close()
