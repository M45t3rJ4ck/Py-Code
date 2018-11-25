####################################################################################
# ========================
# Part 2: Tic-tac-toe
# ========================

# In this task you will be writing a simple game of tic-tac-toe.
# You should expect to find this exercise more challenging than Part 1.
# Please write docstrings for each class and method.
# As you walk through each element, think about how the game's objects are
# organized.
# Does it seem like the most efficient way to do things to you?
# A common criticism of object-oriented programming is that it can lead to
# excessive abstractions and overcomplication.

# =========================
# The TicTacToeBoard class
# =========================

# Write a TicTacToeBoard class definition.
# Your definition should include:
import turtle

X = "X"
O = "O"
EMPTY = " "

board = []
moves = []

grid_pos = 9
grid_choice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
entries = 9 * [0]
    
class TicTacToeBoard(object):
 
    def canvas():
        t = turtle.Pen()
        t.speed(300),t.pu(),t.goto(-150,-150),t.pd()

        canvas = turtle.Screen()
        canvas.setup(800,400)
        canvas.title("Tic Tac Toe")
        
    def square():
        for i in range(0, 4):
            t.forward(100)
            t.left(90)

    def grid():
        for i in range(0, 3):
            square()
            t.forward(100)
        grid(),t.pu(),t.goto(-150,-50),t.pd()
        grid(),t.pu(),t.goto(-150,50),t.pd()
        grid(),t.ht()

    def display_board(board):
        t.up()
        grid_pos = {1:(-100, 100), 2:(0, 100), 3:(100, 100),
                    4:(-100, 0), 5:(0, 0), 6:(100, 0),
                    7:(-100, -100), 8:(0, -100), 9:(100, -100)}            
        if choice in grid_pos:
            t.setpos(grid_pos[choice])
            entries[choice - 1] = seal
            t.pd()
            t.write(seal, font = ("Arial", 30, "bold"))
            if checkForwin(grid_pos, seal):
                has_won(seal)
    
    def legal_move(board):
        for square in range(grid_pos):
            if board[sqaure] == EMPTY:
                moves.append(square)
        return moves

    def checkForwin(board):
        if entries[0] == entries[1] == entries[2] == player or \
            entries[3] == entries[4] == entries[5] == player or \
            entries[6] == entries[7] == entries[8] == player:
            return True
        elif entries[0] == entries[3] == entries[6] == player or \
            entries[1] == entries[4] == entries[7] == player or \
            entries[2] == entries[5] == entries[8] == player:
            return True
        elif entries[0] == entries[4] == entries[8] == player or \
            entries[2] == entries[4] == entries[7] == player:
            return True
        return False
        
# ========================
# The Piece class
# ========================

# Write an abstract Piece class definition.
# Your definition should include:

class Piece(object):

    pieces = []

    def __init__(self):
        self.piece = a

    def main():
        player2, player1 = pieces()
        turn = X   

        while not winner(board):
            if turn == player1:
                move = player1_move(board, player1)
                board[move] = player1
            else:
                move = player2_move(board, player2, player1)
                board[move] = player2
            display_board(board)
            turn = next_turn(turn)

        the_winner = checkForwin(entries, player)

    def next_turn(turn):
        if turn == X:
            return O
        else:
            return X
           
        
    def has_won(player):
        print("Congrats %s's, you have won!" % seal)
  
# =======================
# The X and O classes
# =======================

# Write definitions of X and O piece classes.
# Your definitions should include:

class X(Piece):
    while grid_choice != []:
        x = TicTacToeBoard(canvas).numinput("Player 1 to choose a grid: ", " ", 9, 1)
        while x not in grid_choice:
            x = TicTacToeBoard(canvas).numinput("Player 1 to choose a grid again: ", " ", 9, 1)
    grid_choice.remove(x)
    X(x, "X")

class O(Piece):
    while grid_choice !=[]:
        y = TicTacToeBoard(canvas).numinput("Player 2 to choose a grid: ", " ", 9, 1)
        while y not in grid_choice:
            y = TicTacToeBoard(canvas).numinput("Player 2 to choose a grid again: ", " ", 9, 1)
        grid_choice.remove(y)
        O(y, "O")
