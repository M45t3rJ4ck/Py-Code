# =========================
# Overview
# =========================
# In this exercise you will use what you have learned to implement a Vector
# class and a complex number class.

# ========================
# The Vector class
# ========================
# Write definitions for a class called Vector.
# Your definition should include a constructor,  __str__, values for the x and y
# coordinates, and methods for addition and subtraction of vectors, scalar
# multiplication, length, and comparison.


import math


class Vector(object):

    vector = []
    
    def __init__(self, A):
        self.vector = A

    def getVector(self):
        return self.vector                

    def add(self, vector_B):
        add_Vector = []
        vectorb = vector_B.getVector()
        add_Vector.append(self.vector[0] + self.vectorb[0])
        add_Vector.append(self.vector[1] + self.vectorb[1])
        return add_Vector

    def sub(self, vector_B):
        sub_Vector = []
        sub_Vector.append(self.vector[0] + (-vector_B.getVector()[0]))
        sub_Vector.append(self.vector[1] + (-vector_B.getVector()[1]))
        return sub_Vector

    def SC_Mult(self, scalar):
        SC_Mult_Vector = []
        SC_Mult_Vector.append((self.vector[0]).__mul__(scalar))
        SC_Mult_Vector.append((self.vector[1]).__mul__(scalar))
        return SC_Mult_Vector

    def Length(self):
        Length_Vector = []
        Length_Vector.append((math.sqrt(pow(self.vector[0], 2).__add__(pow(self.vector[1], 2)))))
        return Length_Vector

    def Comparison(self, other):
        if self.Length == other.Length:
            return True
        else:
            return False

    def __str__(self):
        return "The coordinates are: \nX: " + str(self.vector[0]) + " Y: " + str(self.vector[1])

# =========================
# The derived Complex class
# =========================
# Write definitions for a class called MyComplex that is derived from your
# Vector class.  Your definition should include methods for multiplying two
# complex numbers and computing the complex conjugate as well as an updated
# definition of __str__.


class MyComplex(Vector):        

    V_a = []
    V_b = []
    C_a = []
    C_b = []
    C_s = []
    scalar = []
    s_line = []

    def Input(V_a, V_b, scalar, C_a, C_b, C_s):
        V_a.append(float(input("Please enter X1 coordinates: ")))
        V_a.append(float(input("Please enter Y1 coordinates: ")))
        V_b.append(float(input("Please enter X2 coordinates: ")))
        V_b.append(float(input("Please enter y2 coordinates: ")))
        scalar.append(float(input("Please enter any number: ")))
        C_a.append(float(input("Enter a number for Real factor: ")))
        C_a.append(float(input("Enter a number for Imaginary factor: ")))
        C_s.append(input("Enter an operating symbol: "))
        C_b.append(float(input("Enter another Real factor number: ")))
        C_b.append(float(input("Enter another Imaginary factor number: ")))

    def Multi(self, num, sym, s_line):
        real_num = self.vector[0] * num.getVector()[0]
        imag_num = self.vector[1] * num.getVector()[1]
        s_line.append(str(real_num) + " " + sym + " " + str(imag_num) + "i")
        return s_line

    def Computing(self, sym):
        if sym == "+":
            return "Answer: " + str(self.vector[0]) + " + " + str(slef.vector[1])
        else:
            return "Answer: " + str(self.vector[0]) + " - " + str(self.vector[1])

    def __str__(self, sym, Sum, Sub, Mult, Len, prog, Prog, s_line, C_s, com):
        print("Addition of vectors for X is: " + str(Sum[0]) + " and Y is: " + str(Sum[1]))
        print("Subtraction of vectors for X is: " + str(Sub[0]) + " and Y is: " + str(Sub[1]))
        print("Multiplication of vectors for X is: " + str(Mult[0]) + " and Y is: " + str(Mult[1]))
        print("Length of vectors are: " + str(Len[0]))
        print("Compaired to one another: " + str(prog.Comparison(Prog)))
        print("Complex number Multiplication is: " + s_line)
        print("Computing: " + com.Computing(C_s))                        
        print("The complex conjugate is: " + str(self.vector[0]) + " " + sym + str(self.vector[1]))

    def main():
        prog = Vector(MyComplex.V_a)
        Prog = Vector(MyComplex.V_b)
        Sum = prog.add(Prog)
        Sub = prog.sub(Prog)                        
        Mult = prog.SC_Mult(MyComplex.scalar)
        Len = prog.Length()
        com = MyComplex(MyComplex.C_a)
        Com = MyComplex(MyComplex.C_b)
        s_line = com.Multi(MyComplex.Com, MyComplex.C_s)


MyComplex.main()
input("\n\nPress enter to quit.")
