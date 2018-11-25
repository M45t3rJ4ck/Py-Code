#Get user input:
friend_name = input("Enter your a friends full names: ")
friends_age = int(input("Enter your a friends age: "))
#Define operation variables:
friends_names = ["John Doe", "Doe Donald", "Donald Johnson"]
friends_names.append(friend_name)
friends_ages = [35,54,43]
friends_ages.append(friends_age)
#Out Operations:
print(friends_names[0])
print(friends_names[2])
print(len(friends_names))
print(friends_ages)
