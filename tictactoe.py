from random import randint
import time


def start():
    print("Heads or Tails?")
    pick = input()
    value = randint(0, 1)
    flip = ""
    if value == 0:
        flip = "heads"
    else:
        flip = "tails"
    start = ""
    if pick.lower() == flip:
        start = "user"
        print("It was", flip, end=",")
        print(" User starts. User - X    Computer - O")
    else:
        start = "computer"
        print("It was", flip, end=",")
        print(" Computer starts. User - O   Computer - X")
    return start

def userMove(board, user):
    print("Enter location of move: ")
    location = input()
    validInput = False
    while not validInput:
        validInput = True
        if location == "1a" and board[0] == " ":
            board[0] = user
        elif location == "2a" and board[1] == " ":
            board[1] = user
        elif location == "3a" and board[2] == " ":
            board[2] = user
        elif location == "1b" and board[3] == " ":
            board[3] = user
        elif location == "2b" and board[4] == " ":
            board[4] = user
        elif location == "3b" and board[5] == " ":
            board[5] = user
        elif location == "1c" and board[6] == " ":
            board[6] = user
        elif location == "2c" and board[7] == " ":
            board[7] = user
        elif location == "3c" and board[8] == " ":
            board[8] = user
        else:
            print("Invalid move, try again")
            validInput = False
            location = input()

def computerMove(board, computer):
    print("Computer turn")
    time.sleep(2)
    if computer == "X":
        other = "O"
    else:
        other = "X"
    if board[0] == other and board[1] == other and board[2] == " ":
        board[2] = computer
    elif board[1] == other and board[2] == other and board[0] == " ":
        board[0] = computer
    elif board[0] == other and board[2] == other and board[1] == " ":
        board[1] = computer
    elif board[3] == other and board[4] == other and board[5] == " ":
        board[5] = computer
    elif board[4] == other and board[5] == other and board[3] == " ":
        board[3] = computer
    elif board[3] == other and board[5] == other and board[4] == " ":
        board[0] = computer
    elif board[6] == other and board[7] == other and board[8] == " ":
        board[8] = computer
    elif board[7] == other and board[8] == other and board[6] == " ":
        board[6] = computer
    elif board[6] == other and board[8] == other and board[7] == " ":
        board[7] = computer
    elif board[0] == other and board[3] == other and board[6] == " ":
        board[6] = computer
    elif board[0] == other and board[6] == other and board[3] == " ":
        board[3] = computer
    elif board[3] == other and board[6] == other and board[0] == " ":
        board[0] = computer
    elif board[1] == other and board[4] == other and board[7] == " ":
        board[7] = computer
    elif board[4] == other and board[7] == other and board[1] == " ":
        board[1] = computer
    elif board[1] == other and board[7] == other and board[4] == " ":
        board[4] = computer
    elif board[2] == other and board[5] == other and board[8] == " ":
        board[8] = computer
    elif board[2] == other and board[8] == other and board[5] == " ":
        board[5] = computer
    elif board[5] == other and board[8] == other and board[2] == " ":
        board[2] = computer
    elif board[0] == other and board[4] == other and board[8] == " ":
        board[8] = computer
    elif board[0] == other and board[8] == other and board[4] == " ":
        board[4] = computer
    elif board[4] == other and board[8] == other and board[0] == " ":
        board[0] = computer
    elif board[2] == other and board[4] == other and board[6] == " ":
        board[6] = computer
    elif board[2] == other and board[6] == other and board[4] == " ":
        board[4] = computer
    elif board[4] == other and board[6] == other and board[2] == " ":
        board[2] = computer
    else:
        value = randint(0,9)
        while board[value] != " ":
            value = randint(0,9)
        board[value] = computer


def checkIfWon(board):
    won = False
    if (board[0] == "X" and board[1] == "X" and board[2] == "X") or (board[0] == "O" and board[1] == "O" and board[2] == "O"):
        won =True
    elif(board[3] == "X" and board[4] == "X" and board[5] == "X" or board[3] == "O" and board[4] == "O" and board[5] == "O"):
        won =True
    elif(board[6] == "X" and board[7] == "X" and board[8] == "X" or board[6] == "O" and board[7] == "O" and board[8] == "O"):
        won =True
    elif (board[0] == "X" and board[3] == "X" and board[6] == "X" or board[0] == "O" and board[3] == "O" and board[6] == "O"):
        won =True
    elif (board[1] == "X" and board[4] == "X" and board[7] == "X" or board[1] == "O" and board[4] == "O" and board[7] == "O"):
        won = True
    elif (board[2] == "X" and board[5] == "X" and board[8] == "X" or board[2] == "O" and board[5] == "O" and board[8] == "O"):
        won =True
    elif (board[0] == "X" and board[4] == "X" and board[8] == "X" or board[0] == "O" and board[4] == "O" and board[8] == "O"):
        won = True
    elif (board[2] == "X" and board[4] == "X" and board[6] == "X" or board[2] == "O" and board[4] == "O" and board[6] == "O"):
        won = True
    return won

def checkIfDraw(board):
    empty = True
    for x in board:
        if x == " ":
            empty = False
    return empty

def printBoard(board):
    print('    1   2   3')
    print('a   ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   ------------')
    print('b   ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   ------------')
    print('c   ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print("\n")

def main():
    board = [" "," "," "," "," "," "," "," "," "," "]

    firstMove = start()
    if firstMove == "user":
        user = "X"
        computer = "O"
        userMove(board, user)
        printBoard(board)
    elif firstMove == "computer":
        computer = "X"
        user = "O"
        computerMove(board, computer)
        printBoard(board)
    endGame = False
    while not endGame:
        if firstMove == "user":
            computerMove(board, computer)
            printBoard(board)
            if checkIfWon(board):
                print("Computer Wins!")
                endGame=True
                break
            elif checkIfDraw(board):
                print("Its a draw!")
                break
            userMove(board, user)
            printBoard(board)
            if checkIfWon(board):
                print("User Wins!")
                endGame =True
                break
            elif checkIfDraw(board):
                print("Its a draw!")
                break
        elif firstMove == "computer":
            userMove(board, user)
            printBoard(board)
            if checkIfWon(board):
                print("User Wins!")
                endGame =True
                break
            elif checkIfDraw(board):
                print("Its a draw!")
                break
            computerMove(board, computer)
            printBoard(board)
            if checkIfWon(board):
                print("Computer Wins!")
                endGame=True
                break
            elif checkIfDraw(board):
                print("Its a draw!")
                break
    print("\n")

main()
