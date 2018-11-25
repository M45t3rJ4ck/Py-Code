import random

word = "antidisestablishmentarianism"
wordList = list(word)

print("The Word is:",word,"\n")

lengthWord = len(word)
usedValues=[]

for i in range(5):
    position = random.randrange(0,lengthWord)
    print("word[",position, "]\t", word[position])
    usedValues.append(position)

for index in usedValues:
    wordList.pop(index)

print("The remaining letters are",wordList, sep='')
