#Ask user for restaurant
favRest = input("Please enter your favourite restaurant: ")

#Ask user for numbers
intFav = int(input("Please enter your favourite number: "))

#Print out inputs
print("Your favourite kitchen is: {}!".format(favRest))
print("Your lucky number is: {}".format(intFav))

#cast to int
if favRest == int(favRest):
    print("It works!")
elif favRest != int(favRest):
    print("It didn't work...")
else:
    print("You were right!")
