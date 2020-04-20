#-----Global Variables-----

board = ["-","-","-",
         "-","-","-",
         "-","-","-" ]

game_still_going = True

winner = None

current_player = "X"

error = "Input should be a positive integer."

win_number_1 = 0
win_number_2 = 0

#----- Description-----

rules = """
Rules:          
            1. The game is played by 2 players on a grid that's 3 squares by 3 squares.
            2. The first player is X, the second is O. Players take turns putting their marks in empty squares.
            3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
            4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
            5. Type "quite" to quite the game while playing.
            """

help = """Help: 
            Select the square you want to put your X or o into by choosing a number from 1 to 9.  
            You cannot occupy a square that is already occupied. 
            The first player to get three squares in a row wins."""


def score_board():
    global winner
    global win_number_1
    global win_number_2


    if winner == "X":
        win_number_1 = win_number_1 + 1
    elif winner =="O":
        win_number_2 = win_number_2 + 1
    else:
        win_number_1 = win_number_1
        win_number_2 = win_number_2

    print("""
Number of wins: """)
    print(player_1 + " = " + str(win_number_1))
    print(player_2 + " = " + str(win_number_2))


def display_board():
    print("___________________________________")
    print("|    "+board[0] + "     | " + "    "+board[1] + "     | " +"    "+ board[2]+"     |")
    print("|___(1)____|____(2)____|____(3)____|")
    print("|    "+board[3] + "     | " + "    "+board[4] + "     | " +"    "+ board[5]+"     |")
    print("|___(4)____|____(5)____|____(6)____|" )
    print("|    "+board[6] + "     | " + "    "+board[7] + "     | " +"    "+ board[8]+"     |")
    print("|___(7)____|____(8)____|____(9)____|" )


def play_game():

    global player_name

    global  winner

    display_board()

    while game_still_going:

         turn()

         check_if_game_over()

         change_player()


    if winner == "X":
        print("Congratulations!! " + player_1 + " won.")
    elif winner == "O":
        print("Congratulation!! " + player_2 + " won.")
    else:
        print("It's a Tie.")
    score_board()


def turn():

    print(player_name + "'s turn" + "("+ current_player +")")

    #inpt = True
    valid = True
    while valid:
        inpt = True
        while inpt:
            try:
                print(" Type 'help' or 'rules' if needed")
                position = input(" Choose a position from 1 to 9: ")
                position = int(position)
                inpt = False
                #break
            except:
                if position.lower() == "help":
                    print(help)
                    display_board()
                    print(player_name + "'s turn" + "("+ current_player +")")
                elif position.lower() == "rules":
                    print(rules)
                    display_board()
                    print(player_name + "'s turn" + "("+ current_player +")")
                elif position.lower() == "quite":
                    print(player_name + " has quite the game. Thank you for playing")
                    exit()
                else:
                    display_board()
                    print(player_name + "'s turn" + "("+ current_player +")")
                    print(error)



        while position not in [1,2,3,4,5,6,7,8,9]:
            try:
                display_board()
                print(player_name + "'s turn" + "("+ current_player +")")
                print("Invalid Position")
                print(" Type 'help' or 'rules' if needed")
                position = input("Choose a position from 1 to 9: ")
                position = int(position)
            except:
                onpt = True
                if position.lower() == "help":
                    display_board()
                    print(player_name + "'s turn" + "("+ current_player +")")
                    print(help)
                elif position.lower() == "rules":
                    display_board()
                    print(player_name + "'s turn" + "("+ current_player +")")
                    print(rules)
                elif position.lower() == "quite":
                    print(player_name + " has quite the game. Thank you for playing")
                    exit()
                else:
                    display_board()
                    print(player_name + "'s turn" + "("+ current_player +")")
                    print(error)
                while onpt:
                    try:
                        print(" Type 'help' or 'rules' if needed")
                        position = input(" Choose a position from 1 to 9: ")
                        position = int(position)
                        onpt = False
                        #break
                    except:
                        if position.lower() == "help":
                            display_board()
                            print(player_name + "'s turn" + "("+ current_player +")")
                            print(help)
                        elif position.lower() == "rules":
                            display_board()
                            print(player_name + "'s turn" + "("+ current_player +")")
                            print(rules)
                        elif position.lower() == "quite":
                            print(player_name + " has quite the game. Thank you for playing")
                            exit()
                        else:
                            display_board()
                            print(player_name + "'s turn" + "("+ current_player +")")
                            print(error)
        position = int(position) - 1

        if board[position] != "-":
            display_board()
            print(player_name + "'s turn" + "("+ current_player +")")

        if board[position] == "X":
            display_board()
            print(player_name + "'s turn" + "("+ current_player +")")
            print("Position already taken by " + player_1)
        elif board[position] == "O":
            display_board()
            print(player_name + "'s turn" + "("+ current_player +")")
            print("Position already take by " + player_2)
        else:
            valid = False

    board[position] = current_player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():

    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diaganol_winner = check_diaganol()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diaganol_winner:
        winner = diaganol_winner

    else:
        winner = None

    return


def check_rows():

    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]

    elif row_2:
        return board[3]

    elif row_3:
        return board[6]

    return


def check_columns():

    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]

    elif column_2:
        return board[1]

    elif column_3:
        return board[2]

    return


def check_diaganol():

    global game_still_going

    diaganol_1 = board[0] == board[4] == board[8] != "-"
    diaganol_2 = board[2] == board[4] == board[6] != "-"

    if diaganol_1 or diaganol_2:
        game_still_going = False

    if diaganol_1:
        return board[0]

    elif diaganol_2:
        return board[2]

    return


def check_if_tie():

    #global board

    global game_still_going

    if "-" not in board:
        game_still_going = False

    return


def change_player():

    global previous_player
    global current_player
    global player_name

    if current_player =="X" and player_name == player_1 and previous_player == player_2:
        current_player = "O"
        player_name = player_2
        previous_player = player_1
        return

    elif current_player =="O" and player_name == player_2 and previous_player == player_1:
        current_player = "X"
        player_name = player_1
        previous_player = player_2
        return
    return

app_going = True

def initial_play():

    global previous_player
    global player_name
    global player_1
    global player_2
    global app_going

    print("Welcome to the game of TIC TAC TOE")

    while app_going:
        play = input("Do you want to play the game? Type 'yes' or 'no': ")
        if play.lower() == "yes":
            print(rules)

            player_1 = input("Enter Player 1's name: ")
            player_2 = input("Enter Player 2's name: ")

            previous_player = player_2
            player_name = player_1

            play_game()
            restart()

        elif play.lower() == "no":
            exit()
        else:
            print("Invalid Input")
    return

def restart():
    #initial_play()
    global board
    global game_still_going
    global current_player
    global player_name
    global previous_player

    while True:
        play_again = input("Do you want to play again? Type yes or no: ")
        if play_again.lower() == "yes":
            board.insert(0,"-")
            board.insert(1,"-")
            board.insert(2,"-")
            board.insert(3,"-")
            board.insert(4,"-")
            board.insert(5,"-")
            board.insert(6,"-")
            board.insert(7,"-")
            board.insert(8,"-")

            player_name = player_1
            previous_player = player_2
            current_player = "X"
            game_still_going = True

            play_game()
        elif play_again.lower() == "no":
            exit()
        else:
            print("Invalid Input")
    return

#restart()
initial_play()















#board
#display board
#play game
# handle turn
# check win
   #check rows
   #check columns
   #check diagnols
# check tie
#flip player
