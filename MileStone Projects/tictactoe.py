import random
#Displays the board
def display_board(board):
    print("{}|{}|{}".format(board[1],board[2],board[3]))
    print("-|-|-")
    print("{}|{}|{}".format(board[4],board[5],board[6]))
    print("-|-|-")
    print("{}|{}|{}".format(board[7],board[8],board[9]))

#Decides if the marker is an "X" or "O"
def player_input():
    marker = ""

    #Ask Player 1 for their marker until the choose it
    while marker != "X" and marker != "O":
        marker = input("Player 1, please choose a marker("X" or "O"):\n")

    #Set Player 2 to be the opposite of Player 1's marker
    player1 = marker

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return(player1,player2)

#takes in the board, a marker, and position and assigns it to the board
def place_marker(board,marker,position):
    board[position] = marker

#checks to see if someone has won yet
def win_check(board,marker):
    #1,2,3
    if board[1] == board[2] == board[3] == marker:
        return True
    #4,5,6
    elif board[4] == board[5] == board[6] == marker:
        return True
    #7,8,9
    elif board[7] == board[8] == board[9] == marker:
        return True
    #1,4,7
    elif board[1] == board[4] == board[7] == marker:
        return True
    #2,5,8
    elif board[2] == board[5] == board[8] == marker:
        return True
    #3,6,9
    elif board[3] == board[6] == board[9] == marker:
        return True
    #1,5,9
    elif board[1] == board[5] == board[9] == marker:
        return True
    #3,5,7
    elif board[3] == board[5] == board[7] == marker:
        return True
    else:
        return False

#Randomly selects the first player
def choose_first():
    #coin flip between 0 and 1
    selection = random.randint(0,1)

    if selection == 0:
        return "Player 1"
    else:
        return "Player 2"

#checks if the position on the board is free
def space_check(board, position):
    return board[position] == " "

#checks if the entire board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board is full so this is the only other option
    return True

#returns player position choice and checks if its in range and allowable,
def player_choice(board):
    pos = 0
    #while not in range or not on a free position
    while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board,pos):
        pos = int(input("Choose a position(1-9):"))
    return pos

def replay():
    choice = input("Play Again?(Y/N):")
    if(choice == "Y"):
        return "True"
    else:
        return "False"

print("WELCOME TO TIC-TAC-TOE!")

#while loop to keep the game running
while True:

    the_board = [" "]*10

    #calls player_input() to choose markers
    player1_marker,player2_marker = player_input()

    #calls choose_first() to select the first player
    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Ready?(Y/N):")
    if play_game == "Y":
        game_on = True
    else:
        game_on = False


    while game_on:
    ###########GAME START#############
        #PLAYER 1
        if turn == "Player 1":

            #Show the board
            display_board(the_board)
            #Choose position
            position = int(input("Choose a position:(1-9)"))
            place_marker(the_board,player1_marker,position)
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 wins!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!!")
                    game_on = False
                else:
                    turn = "Player 2"
            #player 2 turn
        else:

                #Show the board
                display_board(the_board)
                #Choose position
                position = int(input("Choose a position:(1-9)"))
                place_marker(the_board,player2_marker,position)
                #check if they won
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print("Player 2 wins!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("TIE GAME!!!")
                        game_on = False
                    else:
                        turn = "Player 1"




    #break out of while loop is replay = False
    if not replay():
        break
