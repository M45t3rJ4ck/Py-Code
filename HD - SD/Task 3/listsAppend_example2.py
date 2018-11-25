
listOne = [1,2]

listOne.append(3)

print (listOne) #listOne is now [1,2,3]. The append command adds items to the END of the current list.


newNumList = [1,2,3,4]
copyList = [] #Defines an empty copyList

#If we want to copy all the values in the first list into the second list, we can use the append command as follows:

for num in newNumList:
	copyList.append(num)

print (copyList) #[1,2,3,4]

#The ability of copyList to grow from a list of size 0 to a list of size 4 means that its length is DYNAMIC (can change).
#This makes lists in Python very flexible to use. 
