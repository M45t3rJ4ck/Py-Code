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
# cmath and polar coordinates

class Vector(object):
    
# =========================
# The derived Complex class
# =========================

# Write definitions for a class called MyComplex that is derived from your
# Vector class.  Your definition should include methods for multiplying two
# complex numbers and computing the complex conjugate as well as an updated
# definition of __str__.

class MyComplex(Vector):
        
####################################################################################
# ========================
# Part 2: Tic-tac-toe
# ========================

# In this task you will be writing a simple game of tic-tac-toe.
# You should expect to find this exercise more challenging than Part 1.
# Please write docstrings for each class and method.
# As you walk through each element, think about how the game's objects are organized.
# Does it seem like the most efficient way to do things to you?
# A common criticism of object-oriented programming is that it can lead to
# excessive abstractions and overcomplication.

# ========================
# The Piece class
# ========================

# Write an abstract Piece class definition.
# Your definition should include:

class Piece(object):
    pass

# =======================
# The X and O classes
# =======================

# Write definitions of X and O piece classes.
# Your definitions should include:

class X(Piece):
    pass

class O(Piece):
    pass

# =========================
# The TicTacToeBoard class
# =========================

# Write a TicTacToeBoard class definition.
# Your definition should include:

class TicTacToeBoard(object):
    pass


