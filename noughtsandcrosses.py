# Coursework Assessment 2
# Name: Apoki Efe Prayer
# Student No: 2123563



import random
import os.path
import json
random.seed()

def draw_board(board):
    print(f'\t-----------')
    print(f'\t|{board[0][0]} | {board[0][1]} | {board[0][2]}|')
    print(f'\t---+---+---')
    print(f'\t|{board[1][0]} | {board[1][1]} | {board[1][2]}|')
    print(f'\t---+---+---')
    print(f'\t|{board[2][0]} | {board[2][1]} | {board[2][2]}|')
    print(f'\t-----------')
    pass

def welcome(board):
    print('Welcome to the "Unbeatable Noughts and crosses" game')
    print('The board layout is shown below:')
    draw_board(board)
    print('When prompted, enter the number corresponding to the square you want.')
    pass

def initialise_board(board):
    for row in range(0, 3):
        for col in range(0, 3):
            board[row][col] = ' '
    return board

def get_player_move(board):
    move = input('\t\t '' '' '' 1 2 3\n \t\t '' '' '' 4 5 6\nChoose your square: 7 8 9 :')
    while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print("Invalid Square!.")
        draw_board(board)
        move = input('\t\t '' '' '' 1 2 3\n \t\t '' '' '' 4 5 6\nChoose your square: 7 8 9 :')
    move = int(move) - 1
    row = move // 3
    col = move % 3
    if board[row][col] == " ":
        board[row][col] = "X"
        print('Your turn: ' '\n' 'You played', 'row', row , 'col', col)
    else:
        print("Sorry this cell is already taken... Try again!")
        draw_board(board)
        return get_player_move(board)
    draw_board(board)
    return row, col


def choose_computer_move(board):
    move = random.randint(1, 9)
    move = int(move) - 1
    row = move // 3
    col = move % 3
    if board [1][1] == " ":
        board[1][1] = "O"
        print('Computer turn: ', '\n' 'computer played', 'row', 1 , 'col', 1)
    elif board[row][col] == " ":
        board[row][col] = "O"
        print('Computer turn: ', '\n' 'computer played', 'row', row , 'col', col)
    else:
        return choose_computer_move(board)
    draw_board(board)
    return row, col



def check_for_win(board, mark):
    # Checking the first row...
    if board[0][0] == mark and board[0][1] == mark and board[0][2] == mark:
        return True
        # Checking the second row...
    if board[1][0] == mark and board[1][1] == mark and board[1][2] == mark:
        return True
        # Checking the third row...
    if board[2][0] == mark and board[2][1] == mark and board[2][2] == mark:
        return True
        # Checking the first column
    if board[0][0] == mark and board[1][0] == mark and board[2][0] == mark:
        return True
        # Checking the second column
    if board[0][1] == mark and board[1][1] == mark and board[2][1] == mark:
        return True
        # Checking the third column
    if board[0][2] == mark and board[1][2] == mark and board[2][2] == mark:
        return True
        # Checking the first diagonal
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
        # Checking the second diagonal
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    return False

def check_for_draw(board):
    for spaces in board:
        for item in spaces:
            if item == ' ':
                return False
    return True


def play_game(board):
    print("The game begins!")
    initialise_board(board)
    draw_board(board)
    while True:
        get_player_move(board)
        if check_for_win(board, 'X'):
            print("Congratulations!!. You won the game!.")
            return 1
            break
        if check_for_draw(board):
            print("Match Draw!")
            return 0
            break
        choose_computer_move(board)
        if check_for_win(board, 'O'):
            print("You lost against the computer ): . Try again next time!")
            return -1
            break
        if check_for_draw(board):
            print("Match Draw!")
            return 0
            break
    return 0


def menu():
    while True:
        print('Enter one of the following options.')
        print('\t 1 - Play the game')
        print('\t 2 - Save your Score in the Leaderboard')
        print('\t 3 - Load and display the Leaderboard')
        print('\t q - End the Program')
        choice = input('Enter an option :')
        if choice in ('1', '2', '3', '4', 'q'):
            return choice
        else:
            print("Invalid option entered. Try again!.")
    return choice


def load_scores():
    filename = 'leaderboard.txt'
    if os.path.exists(filename):
        with open(filename, "r") as file:
            dictionary = json.load(file)
            for (key,values) in dictionary.items():
                dictionary[key]=values
                leaders = dictionary
    return leaders


def save_score(score):
    filename = 'leaderboard.txt'
    player = input('what is your name').capitalize()
    if os.path.exists(filename):
        with open(filename, "r") as leaderboard:
            dictionary = json.load(leaderboard)
        dictionary[player]=score
        with open(filename, "w") as leaderboard:
            json.dump(dictionary,leaderboard)
        print("score"+ " " + str(score)+ " "+ "for" + " " +str(player)+ " "+"saved.")
    return


def display_leaderboard(leaders):
    print("--------- LEADERS BOARD ---------")
    print ('{:<25} {}'.format("Name" ,"Score"))
    lead = {**leaders}
    sort_orders = sorted(lead.items(), key = lambda x:x[1],reverse=True)
    for i in sort_orders:
        print('{:<25} {}'.format(i[0],i[1]))
    print("--------- LEADERS BOARD ---------")
    pass



