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
# excessive abstractions and over complication.

# =========================
# The TicTacToeBoard class
# =========================

# Write a TicTacToeBoard class definition.
# Your definition should include:

X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


class TicTacToeBoard(object):

    def display_instruct(self):
        print("""Welcome to the classic Tic Tac Toe game!"""
              """You will make your move known by entering a number! (0 - 8)
                        6 | 7 | 8
                       -----------
                        3 | 4 | 5
                       -----------
                        0 | 1 | 2
                        """)

    def new_board(self):
        board = []
        for square in range(NUM_SQUARES):
            board.append(EMPTY)
        return board

    def display_board(self, board):
        print("\n\t", board[6], "|", board[7], "|", board[8])
        print("\t", "---------")
        print("\t", board[3], "|", board[4], "|", board[5])
        print("\t", "---------")
        print("\t", board[0], "|", board[1], "|", board[2])

    def legal_moves(self, board):
        moves = []
        for square in range(NUM_SQUARES):
            if board[square] == EMPTY:
                moves.append(square)
        return moves

    def winner(self, board):
        ways_to_win = ((0, 1, 2),
                       (3, 4, 5),
                       (6, 7, 8),
                       (0, 3, 6),
                       (1, 4, 7),
                       (2, 5, 8),
                       (0, 4, 8),
                       (2, 4, 6))

        for row in ways_to_win:
            if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
                winner = board[row[0]]
                return winner

        if EMPTY not in board:
            return TIE

        return None

    def congrats_winner(self, the_winner, computer, player):
        if the_winner != TIE:
            print(the_winner, "won!\n")
        else:
            print("AGGHHH! TIE!")
        if the_winner == computer:
            print("As was predicted, human! I am superior in all regards!")
        elif the_winner == player:
            print("NOOO!!! How is this possible!? This is not the last you've heard of me!!")
        elif the_winner == TIE:
            print("This was your lucky day human, soon we shall meet again!")
            
# ========================
# The Piece class
# ========================

# Write an abstract Piece class definition.
# Your definition should include:


class Piece(object):

    def ask_bool(self, question):
        response = []
        while response not in ("Y", "N"):
            response = str(input(question).upper())
        return response

    def ask_num(self, question, low, high):
        response = []
        while response not in range(low, high):
            response = int(input(question))
        return response

    def pieces(self):
        go_first = Piece.ask_bool("Do you require the first move human? (Y/N): ")
        if go_first == "Y":
            print("\nThen take it...You'll need it!!")
            player = X
            computer = O
        else:
            print("\nHa...Your ego will be your downfall!!")
            computer = X
            player = O
        return computer, player

    def next_turn(self, turn):
        if turn == X:
            return O
        else:
            return X

    def main(self):
        TicTacToeBoard.display_instruct(self.board)
        computer, player = Piece.pieces(self)
        turn = X
        board = TicTacToeBoard.new_board(self.board)
        TicTacToeBoard.display_board(self.board)

        while not TicTacToeBoard.winner(self.board):
            if turn == player:
                move = X.player_move(board)
                board[move] = player
            else:
                move = O.computer_move(board, computer, player)
                board[move] = computer
                TicTacToeBoard.display_board(self.board)
                turn = Piece.next_turn(self.turn)

        the_winner = TicTacToeBoard.winner(self.board)
        TicTacToeBoard.congrats_winner(self.the_winner, self.computer, self.player)
        
# =======================
# The X and O classes
# =======================
# Write definitions of X and O piece classes.
# Your definitions should include:


class X(Piece):

    def player_move(self):
        legal = TicTacToeBoard.legal_moves(self.board)
        move = []
        while move not in legal:
            move = Piece.ask_num("Where will you go hide next? (0 - 8): ", 0, NUM_SQUARES)
            if move not in legal:
                print("That square is taken!")
        return move


class O(Piece):

    def computer_move(self, board, computer, player):
        board = board[:]
        best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
        print("I shall take a square!")

        for move in TicTacToeBoard.legal_moves(self.board):
            board[move] = computer
            if TicTacToeBoard.winner(self.board) == computer:
                print(move)
                return move
            board[move] = EMPTY

        for move in TicTacToeBoard.legal_moves(self.board):
            board[move] = player
            if TicTacToeBoard.winner(self.board) == player:
                print(move)
                return move

        for move in best_moves:
            if move in TicTacToeBoard.legal_moves(self.board):
                print(move)
                return move


if __name__ == '__main__':
    Piece.main()

input("\nPress the enter to quit.")
