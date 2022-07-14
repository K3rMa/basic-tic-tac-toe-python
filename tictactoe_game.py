gameRunning = True

def checkBoard():
    # Diagonal win conditions
    if (board[0] == player) and (board[1] == player) and (board[2] == player):
        print(player + " wins!")
    elif (board[3] == player) and (board[4] == player) and (board[5] == player):
        print(player + " wins!")
    elif (board[6] == player) and (board[7] == player) and (board[8] == player):
        print(player + " wins!")
    # Vertical Win Conditions
    elif (board[0] == player) and (board[3] == player) and (board[6] == player):
        print(player + " wins!")
    elif (board[1] == player) and (board[4] == player) and (board[7] == player):
        print(player + " wins!")
    elif (board[2] == player) and (board[5] == player) and (board[8] == player):
        print(player + " wins!")
    # Cross Win Conditions
    elif (board[0] == player) and (board[4] == player) and (board[8] == player):
        print(player + " wins!")
    elif (board[2] == player) and (board[4] == player) and (board[6] == player):
        print(player + " wins!")


        #prints board using fancy loop :) 
def printBoard():
    print("\n━━━━━━━━━━━━━")
    index = 0
    for x in board:
        index = index + 1
        print("│ " + x,end=' ')
        if (index / 3 == round(index/3)): # check if the division results in an integer (whole number)
            print("│")
            print("━━━━━━━━━━━━━")
player = 'x'
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
printBoard()

while gameRunning:
   var = input("Where to place: ")
   if (int(var) <= 9):
    if (int(var) >= 1):
        if (board[int(var)-1] == ' '):
            board[int(var)-1] = player
            printBoard()
            checkBoard()
            if (player == 'x'):
                player = 'o'
            else:
                player = 'x'
    else:
        print("That's smaller than 1")
   else:
    print("That's bigger than 9")
   
