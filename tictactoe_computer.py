
import random

board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]           #this will hold the X's and O's



def print_board():
    print(board[0], "  | ", board[1], "   |  ", board[2])
    print("------------------")
    print(board[3], "  |  ", board[4], "  |  ", board[5])
    print("------------------")
    print(board[6], "  |   ", board[7], " |  ", board[8])


def check_for_win(player_symbol, list_in):           #need list_in so we can check other lists in computer_move()
    if list_in[0] == player_symbol and list_in[1] == player_symbol and list_in[2] == player_symbol:
        print("Player, ", player_symbol, " wins")
        return True
    elif list_in[3] == player_symbol and list_in[4] == player_symbol and list_in[5] == player_symbol:
        print("Player , ", player_symbol, "wins")
        return True
    elif list_in[6] == player_symbol and list_in[7] == player_symbol and list_in[8] == player_symbol:
        print("Player , ", player_symbol, " wins")
        return True

    elif list_in[0] == player_symbol and list_in[3] == player_symbol and list_in[6] == player_symbol:
        print("Player , ", player_symbol, " wins")
        return True
    elif list_in[1] == player_symbol and list_in[4] == player_symbol and list_in[7] == player_symbol:
        print("Player , ", player_symbol, " wins")
        return True
    elif list_in[2] == player_symbol and list_in[5] == player_symbol and list_in[8] == player_symbol:
        print("Player , ", player_symbol, " wins")
        return True

    elif list_in[0] == player_symbol and list_in[4] == player_symbol and list_in[8] == player_symbol:
        print("Player , ", player_symbol, " wins")
        return True
    elif list_in[2] == player_symbol and list_in[4] == player_symbol and list_in[6] == player_symbol:
        print("Player , ", player_symbol, " wins")
        return True

def computer_move():

    list_copy = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    for i in range(9):                             #copying the board to our list_copy
        list_copy[i] = board[i]

    for i in range(9):                             #checking to see if the computer can win with this move
        if list_copy[i] == "_":
            list_copy[i] = "O"

            if check_for_win("O", list_copy):

                return i
            else:
                list_copy[i] = "_"

    for i in range(9):                            #checking to see if the player can win with their next move
        if list_copy[i] == "_":
            list_copy[i] = "X"
            if check_for_win("X", list_copy):
                return i
            else:
                list_copy[i] = "_"

    if board.count("_") == 8 and board[4] == "X":    #taking a corner on first move if Player chooses center
        options = [0, 2, 6, 8]                       #the corners
        return options[ random.randint(0,3)]         #returns a random corner spot

    while True:                                     #picks a random available spot to play if nothing above is best
        spot = random.randint(0,8)
        if board[ spot ] == '_':
            return spot

def game_tie_check():
    if board.count("_") == 0:
        return True

print_board()

while True:

    while True:
        player1 = int(input("Input a number 0-8 to select where to put your X"))
        if board[player1] == "_":
            board[player1] = 'X'
            break
        else:
            print("Please choose a legal spot")

    print_board()

    if check_for_win('X', board):
        break
    elif game_tie_check():
        print("Cat's game (tie)")
        break

    board[ computer_move() ] = 'O'
    print("Computer's move:  ")
    print_board()

    if check_for_win('O', board):
        break
    elif game_tie_check():
        print("Cat's game (tie)")
        break














