
number = int(raw_input("Enter number less than 100: "))
while number > 100:
    print "Please try again"
    number = int(raw_input("Enter number less than 100: "))
if number%2 == 0:
    print number*2
else:
    print number*3

