print("Welcome to Jay's Tic Tac Toe")
print()
print("Here is the positions of the Tic Tac Toe you must enter while playing the game")
print()
print("1" + "|" + "2" + "|" + "3")
print("-+-+-")
print("4" + "|" + "5" + "|" + "6")
print("-+-+-")
print("7" + "|" + "8" + "|" + "9")

theBoard = {"1" : " ", "2" : " ", "3" : " ",
            "4" : " ", "5" : " ", "6" : " ",
            "7" : " ", "8" : " ", "9" : " ",}

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["7"] + "|" + board["8"] + "|" + board["9"])

def game():
    turn = "X"
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn Player  " + turn + ". Move to which place:  ")

        move = input()

        if theBoard[move] == " ":
            theBoard[move] = turn
            count += 1
        else:
            print()
            print("The place is already filled. \n ove to which place?:  ")
            continue

        if count >= 5:
            if theBoard["1"] + "|" + theBoard["2"] + "|" + theBoard["3"] != " ":
                printBoard(theBoard)
                print()
                print("\n Game Over! \n")
                print("****" + turn + "won. ****")
                break
            elif theBoard["4"] + "|" + theBoard["5"] + "|" + theBoard["6"] != " ":
                printBoard(theBoard)
                print()
                print("\n Game Over! \n")
                print("****" + turn + "won. ****")
                break
            elif theBoard["7"] + "|" + theBoard["8"] + "|" + theBoard["9"] != " ":
                printBoard(theBoard)
                print()
                print("\n Game Over! \n")
                print("****" + turn + "won. ****")
                break
            elif theBoard["1"] + "|" + theBoard["4"] + "|" + theBoard["7"] != " ":
                printBoard(theBoard)
                print()
                print("\n Game Over! \n")
                print("****" + turn + "won. ****")
                break
            elif theBoard["2"] + "|" + theBoard["5"] + "|" + theBoard["8"] != " ":
                printBoard(theBoard)
                print()
                print("\n Game Over! \n")
                print("****" + turn + "won. ****")
                break
            elif theBoard["3"] + "|" + theBoard["6"] + "|" + theBoard["9"] != " ":
                printBoard(theBoard)
                print()
                print("\n Game Over! \n")
                print("****" + turn + "won. ****")
                break
            elif theBoard["7"] + "|" + theBoard["5"] + "|" + theBoard["3"] != " ":
                printBoard(theBoard)
                print()
                print("\n Game Over! \n")
                print("****" + turn + "won. ****")
                break
            elif theBoard["1"] + "|" + theBoard["5"] + "|" + theBoard["9"] != " ":
                printBoard(theBoard)
                print()
                print("\n Game Over! \n")
                print("****" + turn + "won. ****")
                break

        if count == 9:
            print()
            print("\n Game Over!\n")
            print("\n It's a TIE!\n")

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

restart = input("Do you want to play again (y/n)")
if restart == "y" or restart == "Y":
    for key in board_keys:
        theBoard[key] = " "
    game()
else:
    print("Thank You for Playing!")