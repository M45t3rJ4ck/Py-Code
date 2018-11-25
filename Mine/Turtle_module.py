import turtle

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

def Xs_and_Os(choice, seal):

    t.up()
    grid_pos = {1:(-100, 100), 2:(0, 100), 3:(100, 100),
                4:(-100, 0), 5:(0, 0), 6:(100, 0),
                7:(-100, -100), 8:(0, -100), 9:(100, -100)}            

    if choice in grid_pos:
        t.setpos(grid_pos[choice])
        entries[choice-1] = seal
        t.pd()
        t.write(seal, font = ("Arial", 30, "bold"))

        if check_for_win(grid_pos, seal):
            has_won(seal)
        
grid_choice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
entries = [[0], [0], [0],
           [0], [0], [0],
           [0], [0], [0]]

while grid_choice != []:
    x = canvas.numinput( "Player 1, choose a square. ", " ", 9, 1)

    while x not in grid_choice:
        x = canvas.numinput("Player 1, choose again. ", " ", 9, 1)

    grid_choice.remove(x)
    Xs_and_Os(x,"X")

    y = canvas.numinput("\n" + "Player 2, choose a square.  ", " ", 9, 1)

    while y not in grid_choice:
        y = canvas.numinput("\n" + "Player 2, choose again.  ", " ", 9, 1)

    grid_choice.remove(y)
    Xs_and_Os(y, "O")

def checkForwin(entires, player):

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

def has_won(player):

    print("Congrats %s's, you have won!" % seal)
