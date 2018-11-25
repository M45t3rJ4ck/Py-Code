
import random
num = random.randint(1,50)
numGuess = int(raw_input("Guess a number from 1 to 50: "))
while numGuess != num:
    numGuess = int(raw_input("Incorrect. Guess another number from 1 to 50: "))
print "You guessed correctly!"
