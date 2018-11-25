import random as rand

# print([i ** 2 for i in range(50) if i % 8 == 0])

u_in = str(input("Please enter a 5 number sequence: \n"))
nums = [int(i) for i in u_in]
r_num = rand.randint(2, 10)
print(r_num)
sym = "+" or "-"
sum_num = 0
output = True
if sum_num % r_num == 0:
    for num in nums:
        if sym == "+":
            sum_num = sum_num + num
            print(str(sum_num))
        elif sym == "-":
            sum_num = sum_num - num
            print(str(sum_num))
    print(str(output))
elif sum_num % r_num != 0:
    output = False
    print(str(output))
    
# print([int(i) for i in u_in if sum_num % r_num == 0])


