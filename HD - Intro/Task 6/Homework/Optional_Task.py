import math
#Get user input:
side1, side2, side3 = input("Please enter the 3 side of your triangle: ").split()
#Define user input:
side1 = int(side1)
side2 = int(side2)
side3 = int(side3)
#Define Operations:
Sides = (side1 + side2 + side3) / 2
Triarea = math.sqrt(Sides * (Sides - side1) * (Sides - side2) * (Sides - side3))
#Print Operations:
print("{:.2f}".format(Triarea))
