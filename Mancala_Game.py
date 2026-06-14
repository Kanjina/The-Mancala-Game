"""
This is the Mancala game.
This is the fully completed game designed to be played by two players.
"""

#Below is the Code Running Variable, which determines if the
#player plays or not.
Code_Running = True

#This creates a global variable which controls whether the game is on
PlayGame = True

#Creating the global board variable, the initial board with values
board = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]

#This creates the global print assist variable,
# which controls whether or not the player sees the instructions at the beginning of their turn.
print_assist = True


"""
The function below prints the board in a nice format.
Input: The function takes board as an argument.
Output: The function does not return anything, but it will print the board.
"""
def printBoard(board):
    print("  ", "0", "  ", "13", "   ", "12", "   ", "11", "   ", "10", "   ", "9", "    ", "8")
    print("--------------------------------------------------")
    print("B:", "    ", board[13], "    ", board[12], "    ", board[11], "    ", board[10], "    ", board[9], "    ", board[8])
    print("  ", board[0], "                                           ", board[7])
    print("A:", "    ", board[1], "    ", board[2], "    ", board[3], "    ", board[4], "    ", board[5], "    ", board[6])
    print("--------------------------------------------------")
    print("       ", "1", "    ", "2", "    ", "3", "    ", "4", "    ", "5", "    ", "6", "   ", "7")

\
#This creates the global player variable, player A goes first
player = "A"

"""
This function prints the assistance message at the beginning of a player's turn.
Input: The function takes in a boolean arguement, which is the global print assist variable.
Output: If the arguement is true, the function will print the assistance message, which
includes the rules and the surrender option. If the arguement is false,
the function will print a message that tells the player how to see the assistance message again.
"""
def print_assistance(arguement):
    if arguement == True:
        print('Type in "rules" to see the rules of the game')
        print('Type in "surrender" to quit the game')
        print("Warning! Surrendering means that you lose!")
        print('To stop seeing this message, type in "stop" during your turn.')
    else:
        print('Type in "check" to see the reminders again!')

"""
This function prints the rules of the game. It is called when a player types in "rules" (case insensitive) during their turn.
Input: The function takes in two arguements, the first is the title of the rules and the second is a string which is just a space. This is for formatting purposes.
Output: The function prints the rules of the game and the title.
"""
def print_rules(arguement, space):
    print(arguement)
    print(space)
    print("The rules of the game are as follows:")
    print("1. The board consists of 14 pockets, 6 on each side and 2 Mancalas.")
    print("2. Each player has a Mancala on their right and 6 pockets in front of them.")
    print("3. Players take turns picking up all the stones from one of their pockets and distributing them counterclockwise,")
    print("3... one by one, into the subsequent pockets and their own Mancala (but not their opponent's).")
    print("4. If the last stone lands in an empty pocket on the player's side, they capture that stone,")
    print("4... and any stones in the opposite pocket on the opponent's side, placing them in their own Mancala.")
    print("5. If the last stone lands in the player's own Mancala, they get an extra turn.")
    print("6. The game ends when all six pockets on one side of the board are empty.")
    print("7. The player with the most stones in their Mancala wins.")
    print(space)

"""
is_valid_move is a function that checks whether or not the move the player has chosen is valid.
It checks whether the move is a number, whether the move is on the player's side of the board,
and whether or not there are any stones in the pocket that the player has chosen.
is_valid_move returns "pass" if the move is valid, and it returns nothing if the move is invalid.
It also prints out the reason why the move is invalid.

is_valid_move is ran in the take_turn function, which is the function that handles the player's turn.
if is_valid_move returns "pass", then the move is valid and the player can proceed with their turn.
elif is_valid_move does not return "pass", then the player will be prompted to enter a new move until they enter a valid move.

Input: The function takes in the chosen move, a string entered by the player, as an argument.

Output: The function returns "pass" if the move is valid, and it returns nothing if the move is invalid.
It will then print out why the move is invalid.
"""
def is_valid_move(chosen_move):
    if player == "A":
        if 1 <= int(chosen_move) <= 6:
            if board[chosen_move] > 0:
                print("Valid Move!")
                return "pass"
            else:
                print("The pocket you selected has no stones!")
        elif 8 <= int(chosen_move) <= 13:
            print("Those are Player B's pockets!")
        elif int(chosen_move) == 0 or int(chosen_move) == 7:
            print("You can't take stones from a Mancala!")
        else:
            print("Invalid move!")
    else:
        if 8 <= int(chosen_move) <= 13:
            if board[chosen_move] > 0:
                print("Valid Move!")
                return "pass"
            else:
                print("The pocket you selected has no stones!")
        elif 1 <= int(chosen_move) <= 6:
            print("Those are Player A's pockets!")
        elif int(chosen_move) == 0 or int(chosen_move) == 7:
            print("You can't take stones from a Mancala!")
        else:
            print("Invalid move!")

"""
take_turn is the function that handles the player's turn.
It prompts the player to enter a move, and it checks whether the move
is valid using the is_valid_move function.
Input: The function takes in the player, a string which is either "A" or "B", as an argument.
Output: The function returns the chosen move if the move is valid,
and it returns nothing if the move is invalid.
"""
def take_turn(player):
    global PlayGame
    if player == "A":
        print("")
        print("It's Player A's turn!")
        print("")
        print_assistance(print_assist)
        print("")
        """
        Lines 74 - 79 check whether a pocket has or doesn't have
        stones, if it doesn't the pocket number will not be added
        to the list of possible moves
        """
        temp_list = []
        for i in range(1,7):
            if board[i] > 0:
                temp_list.append(i)
            else:
                pass
        """
        Line 83 is the joining of the temporary list created
        in line 73. It will print out the joined list.
        """
        y = ", ".join(str(x) for x in temp_list)
        print("Possible moves: " + y)
        while True:
            chosen_move = input("Enter a pocket number: ")
            try:
                chosen_move = int(chosen_move)
                if is_valid_move(chosen_move) == "pass":
                    return chosen_move
            except ValueError: #The player may surrender
                if chosen_move.lower() == "surrender":
                    PlayGame = False
                    return 32767 #32767 was chosen b/c it's the 16-bit integer limit
                elif chosen_move.lower() == "rules":
                    return 2147483647 #2147483647 was chosen b/c it's the 32-bit integer limit
                elif chosen_move.lower() == "stop":
                    return 1156
                elif chosen_move.lower() == "check":
                    return 939
                else:
                    print("Input must be a board pocket!")
    else:
        print("")
        print("It's Player B's turn!")
        print("")
        print_assistance(print_assist)
        print("")
        temp_list = [] #This code is a repeat of Player A's
        for i in range(8,14): #The same for loop, but with different values.
            if board[i] > 0:
                temp_list.append(i)
            else:
                pass
        y = ", ".join(str(x) for x in temp_list)
        print("Possible moves: " + y)
        while True:
            chosen_move = input("Enter a pocket number: ")
            try:
                chosen_move = int(chosen_move)
                if is_valid_move(chosen_move) == "pass":
                    return chosen_move
            except ValueError:
                if chosen_move.lower() == "surrender":
                    PlayGame = False
                    return 255 #255 was chosen b/c it's the 8-bit integer limit
                elif chosen_move.lower() == "rules":
                    return 2147483647 #2147483647 was chosen b/c it's the 32-bit integer limit
                elif chosen_move.lower() == "stop":
                    return 1156
                elif chosen_move.lower() == "check":
                    return 939
                else:
                    print("Input must be a board pocket!")

"""
move_stones is the longest and most complicated of my functions.
It handles moving the stones and the turn order after a player has chosen a move.

Input: The function takes in the chosen move,
an integer which is the pocket number that the player has chosen to move from, as an argument.

Output: The function does not return anything, but it will change the global board variable
to reflect the new board state after the move has been made.
"""
def move_stones(chosen_move):
    global player #Defining our global variables
    global board
    m = chosen_move

    #NOS stands for Number of Stones
    NOS = board[m]
    new_board = board.copy()


    #This creates a new board where the values of the board are changed
    new_board[m] = 0
    if player == "A":
        for i in range(NOS):
            m = (m + 1) % 14
            while m == 0:
                m = (m + 1) % 14
            new_board[m] += 1
        if new_board[m] == 1 and m in range(1,7):
            new_board[m] = 0
            opposite_m = 14 - m
            temp_val = new_board[opposite_m]
            new_board[opposite_m] = 0
            new_board[7] += (temp_val + 1)
    if player == "B":
        for i in range(NOS):
            m = (m + 1) % 14
            while m == 7:
                m = (m + 1) % 14
            new_board[m] += 1
        if new_board[m] == 1 and m in range(8,14):
            new_board[m] = 0
            opposite_m = 14 - m
            temp_val = new_board[opposite_m]
            new_board[opposite_m] = 0
            new_board[0] += (temp_val + 1)
        
    board[:] = new_board
        
    #Turn order function
    if player == "A":
        if m == 7:
            player = "A"
        else:
            player = "B"
    else:
        if m == 0:
            player = "B"
        else:
            player = "A"
    chosen_move = 0
    m = 0

#The function below checks if any 1 side of the board is empty.
def game_over(board):
    global PlayGame
    #Below is Player A's empty pocket count
    Zero_Count_Player_A = 0
    for pocket in board[1:7]:
        if pocket == 0:
            Zero_Count_Player_A += 1
        else:
            pass
    #Below is Player B's empty pocket count
    Zero_Count_Player_B = 0
    for pocket in board[8:14]:
        if pocket == 0:
            Zero_Count_Player_B += 1
        else:
            pass
    #The Code below will return a value for this function
    #if the win conditions are met.
    if Zero_Count_Player_A == 6:
        return 1
    elif Zero_Count_Player_B == 6:
        return 2
    else:
        return 0
        
#The function below will only run if game_over() returns 1.
#It will calculate which side has more stones at the end.
def calculate_winner():
    global player
    global board
    side = game_over(board)
    PAW = "Game Over! Player A has won!" #Variables which are strings
    PBW = "Game Over! Player B has won!" #This avoids repeating the same
    DRAW = "Game Over! The game is a draw!" #strings over and over.
    if side == 1:
        #PBSC stands for Player B Stone Count
        PBSC = 0
        for i in range(8,14):
            PBSC += board[i]
            board[i] = 0
        PBSC = PBSC + board[0]
        #The code below calculates Player A's Stone Count
        PASC = board[7]
        if PASC > PBSC:
            return PAW
        elif PBSC > PASC:
            return PBW
        else:
            return DRAW
    if side == 2:
        PASC = 0
        for i in range(1,7):
            PASC += board[i]
            board[i] = 0
        PASC = PASC + board[7]
        #The code below calculates Player B's Stone Count
        PBSC = board[0]
        if PASC > PBSC:
            return PAW
        elif PBSC > PASC:
            return PBW
        else:
            return DRAW
"""
The function below will run once a round is finished
It will ask the players whether or not they wish to
continue playing the game.

Input: The function takes in no arguments, but it will ask the player to
input whether or not they wish to continue playing the game.

Output: The function will return 1 if the player wishes to continue playing the game,
and it will return "Halt" if the player wishes to stop playing the game.
"""
def reset_game():
    global board #Setting our variables to be global
    global PlayGame
    global player
    #The while loop has options to reset the board or end the game
    while True:
        print("")
        print('Type "continue" if you wish to play another match.')
        print('Otherwise, please type "halt" if you wish to stop playing.')
        print("")
        variable = input("Enter your choice here: ")
        if variable.lower() == "continue":
            board = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
            PlayGame = True
            player = "A"
            return 1
        elif variable.lower() == '"continue"':
            board = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
            PlayGame = True
            player = "A"
            return 1
        elif variable.lower() == "halt":
            return "Halt"
        elif variable.lower() == '"halt"':
            return "Halt"
        else:
            print("Please type in a valid choice!")
            continue
"""
Code_Running and PlayGame are set to true, meaning that both
while loops run. Code_Running contains all the functions that run the game,
while PlayGame contains the functions that run each round of the game.
"""
while Code_Running:
    while PlayGame:
        printBoard(board)
        chosen_move = take_turn(player)
        if chosen_move in (2147483647, 32767, 255, 1156, 939):
            if chosen_move == 2147483647:
                print_rules("Rules of the Mancala Game", " ")
                continue
            elif chosen_move == 1156:
                print_assist = False
                continue
            elif chosen_move == 939:
                print_assist = True
                continue
            elif chosen_move == 32767:
                print("Game Over! Player B has won!")
                break
            else:
                print("Game Over! Player A has won!")
                break
        move_stones(chosen_move)
        Value = game_over(board)
        if int(Value) > 0:
            PlayGame = False

    #This prints the result of the game.
    if chosen_move != 32767 and chosen_move != 255:
        print(calculate_winner())

    game_reset = reset_game()
    #If reset_game(board) returns halt, the full loop will be exited.
    if game_reset == "Halt":
        Code_Running = False
        print("")
        print("Thank you for playing the Mancala Game!")
        break
    elif game_reset == 1:
        print("") #Will give the new game some space