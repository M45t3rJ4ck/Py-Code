import math


class Vector(object):
    
    vector = []

    def __init__(self, A):
        self.vector = A

    def getVector(self):
        return self.vector

    def addition(self, vector_B):
        add_Vector = []
        vectorb = vector_B.getVector()
        add_Vector.append(self.vector[0] + vectorb[0])
        add_Vector.append(self.vector[1] + vectorb[1])
        return add_Vector
    
    def subtract(self, vector_B):
        sub_Vector = []
        sub_Vector.append(self.vector[0] + (-vector_B.getVector()[0]))
        sub_Vector.append(self.vector[1] + (-vector_B.getVector()[1]))
        return sub_Vector
    
    def multiply(self, scalar):
        mul_Vector = []
        mul_Vector.append(self.vector[0] * scalar)
        mul_Vector.append(self.vector[1] * scalar)
        return mul_Vector
    
    def length(self):
        length_Vector = []
        length_Vector.append(math.sqrt(pow(self.vector[0],2) + pow(self.vector[1],2)))
        return length_Vector

    def comparison(self, other):
        if self.length() ==  other.length():
            return True
        else:
            return False

    def __str__(self):
        return "The Vector Coordinates are: X: " + str(self.vector[0]) + " Y: " + str(self.vector[1])


class MyComplex(Vector):
    
    def Multiply(self, Number, symbol):
        Real_num = self.vector[0] * Number.getVector()[0]
        imaginary_num = self.vector[1] * Number.getVector()[1]
        Soneline = str(Real_num) + " " + symbol + " " + str(imaginary_num) + "i"
        return Soneline

    def Computing(self, symbol):
        if symbol == "+":
            return str(self.vector[0]) + " + " + str(self.vector[1]) 
        else:
            return str(self.vector[0]) + " - " + str(self.vector[1])

    def __str__(self, symbol):
        return "Complex Number is: " + str(self.vector[0]) + " " + symbol + " " + str(self.vector[1])


v_a = []
v_b = []

v_a.append(int(input("Please Enter Vector X Coordinate: ")))
v_a.append(int(input("Please Enter Vector Y Coordinate: ")))


v_b.append(int(input("Please Enter Vector 2 X Coordinate: ")))
v_b.append(int(input("Please Enter Vector 2 Y Coordinate: ")))

program = Vector(v_a)
P1 = Vector(v_b)


Sum = program.addition(P1)
Sub = program.subtract(P1)

print("The Addition for Vector 1 + Vector 2 is: X: " + str(Sum[0]) + " Y: " + str(Sum[1]))
print("The Subtraction for Vector 1 - Vector 2 to is: X: " + str(Sub[0]) + " Y: " + str(Sub[1]))
scalar = int(input("Please enter a Scalar to Multiply Vector: "))
Mul = program.multiply(scalar)
print("The Maltiplication for Vector 1 By: " + str(scalar) + " is: X: " + str(Mul[0]) + " Y: " + str(Mul[1]))
length = program.length()
print("The Length for Vector 1 is: " + str(length[0]))

print("The Comparison is: " + str(program.comparison(P1)))

c_a = []
c_b = []

c_a.append(int(input("Please Enter Real Number: ")))
c_a.append(int(input("Please Enter Imaginary Number: ")))

c_s = input("Please Enter Operation Symbol: ")

c_b.append(int(input("Please Enter Real Number: ")))
c_b.append(int(input("Please Enter Imaginary Number: ")))

Com = MyComplex(c_a)
Com1 = MyComplex(c_b)

Soneline = Com.Multiply(Com1,c_s)

print("The Complex Number Multiply: " + Soneline)

print("Computing: " + Com.Computing(c_s))
