
cleanCarRed = True
cleanCarBlue = True
cleanCarGreen = True
numOfCar = 0
Busy = False

print ("Welcome to the car wash")

redCheck = input("Is the Red car Dirty? (Yes or No)")
if redCheck == "Yes":
	cleanCarRed = False

blueCheck = input("Is the Blue car Dirty? (Yes or No)")
if blueCheck == "Yes":
	cleanCarBlue = False

greenCheck = input("Is the Green car Dirty? (Yes or No)")
if greenCheck == "Yes":
	cleanCarGreen = False	


if cleanCarRed == False:
	print ("Red car really needs a cleaning")
	numOfCar +=1

if cleanCarBlue == False:
	print ("Blue car really needs a cleaning")
	numOfCar +=1


if cleanCarGreen == False:
	print ("Green car really needs a cleaning")
	numOfCar +=1
	print (numOfCar)

if numOfCar == 3:
	Busy = True

if Busy == True:
	print ("The car wash was was packed today")

