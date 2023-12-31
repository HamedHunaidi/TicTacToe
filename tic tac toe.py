import random

board = [
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
]

currentPlayer = "X"
winner = None
gameRunning = True


# print the game board
def printBoard(Board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# take input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currentPlayer

    else:
        print("Spot is taken!")


# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[6]
        return True


def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[5]
        return True


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[4]
        return True


def checkTie():
    if "-" not in board:
        printBoard(board)
        print("It's a TIE!")
        gameRunning = False


def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        print(f"the Winnder is {winner}")
        gameRunning = False


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# ai


def ai(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


# check for win
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie()
    switchPlayer()
    ai(board)
    checkWin()
    checkTie()
