# Willem Adriaan Voges
#Get's the age from user:
age = int(input("Please enter your age: "))
#Checks user's age:
#older than 18:
if age >= 18:
    print("You're old enough!")
#Younger than 18:
elif age <= 17:
    print("You're suppouse to be in bed!!")
    for i in range(0, age):
        if i != 18:
            print(i)
