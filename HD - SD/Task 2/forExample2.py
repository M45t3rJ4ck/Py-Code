#This is an example Python program demonstrating for loops.
#It asks for the user to input a number.
#If the number is even, a for loop prints out an increasing * pattern.
#If the number is odd, a for loop prints out a decreasing * pattern.

input = int(input("Enter a number: "))

if (input % 2 == 0): #If number is even. 

        stars = "*"
        
        for i in range (0 ,10):
                
                stars = stars +"*"
                print (stars)
                
elif (input%2!=0): #If number is odd, ie the number divided by 2 does NOT have a remainder of 0
        
        stars = "**********"
        for i in range (0 ,10):
        
                index = 10-i  #i goes from 0 to 10 in this loop
                
                print (stars[0:index]) #Index gets SMALLER as the loop goes on ie from [0:10] to [0:1] ie fewer of the 10 original stars will be printed out
                
                #Remember you can cut off pieces of a String using string[start index: end index]. 
                
                


	
