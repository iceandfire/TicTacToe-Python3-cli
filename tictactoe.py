"""
TicTacToe written in Python 3
- written by Arham Jamal.
"""
import random


def display_board(board):
    print('\n' * 100)
    print(board[7]+ '|' +board[8] + '|' +board[9])
    print('-----')
    print(board[4]+ '|' +board[5] + '|' +board[6])
    print('-----')
    print(board[1]+ '|' +board[2] + '|' +board[3])


def player_input():
    x = None
    y = None
    while x != 'X' and x != 'O':
        x = input("Player one what would you like to use: X or O? ")

    if x == 'X':
        y = 'O'
    else:
        y = 'X'

    #     print('Player 1 will be '+ x)
    #     print('Player 2 will be '+ y)
    return x, y


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    elif board[7] == board[5] == board[3] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    else:
        return False


def choose_first():
    r1 = random.randint(1, 2)
    if r1 == 1:
        return "Player 1 will go first"
    else:
        return "Player 2 will go first"
    # return r1


def space_check(board, position):
    if board[position] != 'X' and board[position] != 'O':
        return True
    else:
        return False


def full_board_check(board):
    for i in range(1, 10):
        if board[i] != 'X' and board[i] != 'O':
            return False
    else:
        return True


def player_choice(board):
    player_c = int(input('Player please enter your next position as a number between 1 and 9: '))
    if space_check(board, player_c):
        return player_c


def replay():
    play_again = None
    while play_again != "Yes" and play_again != "No":
        play_again = input("Player do you want to play again? Enter Yes or No: ")
        if play_again == "Yes":
            return True
        elif play_again == 'No':
            return False


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board1 = [' ']*10
    x, o = player_input()
    # print(x, o)
    display_board(board1)
    rand = choose_first()
    print(rand)
    #pass

    while not full_board_check(board1):
        #Player 1 Turn
        if rand == "Player 1 will go first":
            ch = player_choice(board1)
            place_marker(board1, x, ch)
            display_board(board1)
            if win_check(board1, x):
                print("Player 1 Won!")
                break
            rand = "Player 2 will go first"
        else:
        # Player2's turn.
            ch = player_choice(board1)
            place_marker(board1, o, ch)
            display_board(board1)
            if win_check(board1, o):
                print("Player 2 Won!")
                break
            rand = "Player 1 will go first"
    else:
        print("Tie")
            #pass
    if not replay():
        break
