from IPython.display import clear_output
import time
import random

def display_board(board):
    
    print(" "+board[7]+"  |  "+board[8]+"  |  "+board[9])
    print("---------------")
    print(" "+board[4]+"  |  "+board[5]+"  |  "+board[6])
    print("---------------")
    print(" "+board[1]+"  |  "+board[2]+"  |  "+board[3])

def player_input():
    while True:
        mark=input("Enter your marker O or X : ").upper()
        if mark == 'X':
            return ("X","O")
        elif mark == 'O':
            return ("O","X")
        else:
            print("Wrong Input!Please try again")
            time.sleep(1)
            clear_output()
            continue

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board,mark):
    return ((mark == board[7] == board[8] == board[9]) or
            (mark == board[3] == board[4] == board[5]) or
            (mark == board[1] == board[2] == board[3]) or
            (mark == board[1] == board[4] == board[7]) or
            (mark == board[2] == board[5] == board[8]) or
            (mark == board[3] == board[6] == board[9]) or
            (mark == board[1] == board[5] == board[9]) or
            (mark == board[7] == board[5] == board[3]))

def choose_first():
    x=random.randint(1,2)
    if x==1:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        if position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
            print("Wrong Input! Please try again.")

    return position

def replay():
    while True:
        play = input("You want to play again?(Y/N) : ").upper()
        if play == 'Y':
            return True
        elif play == 'N':
            return False
        else: 
            print("Wrong Input! Try Again.")



print('Welcome to Tic Tac Toe! -----------------')
print('----------------------- By Deepanshu Jain')
print('                                         ')
print('                                         ')

while True:
    my_board = ["#"," "," "," "," "," "," "," "," "," "]
    print("Player 1")
    player1,player2=player_input()
    clear_output()
    print("Player 1 : "+player1)
    print("Player 2 : "+player2)
    display_board(my_board)
    x=choose_first()
    print(x+" will go first.")
    game_on=True
    while game_on:
        if x == "Player 1":
            print("Player 1 Turn ( "+player1+" )")
            POS = player_choice(my_board)
            while space_check(my_board,POS):
                place_marker(my_board,player1,POS)
                break
            else:
                print("Oops! Try Another Position.")
            time.sleep(1)
            clear_output()
            display_board(my_board)
            if win_check(my_board,player1):
                print("Player 1 Won!")
                game_on = False
            elif full_board_check(my_board):
                print("Oh! Game tied.")
                game_on = False
            else: 
                x = "Player 2"
        
        
        elif x == "Player 2":
            print("Player 2 Turn ( "+player2+" )")
            POS = player_choice(my_board)
            while space_check(my_board,POS):
                place_marker(my_board,player2,POS)
                break
            else:
                print("Oops! Try Another Position.")
            time.sleep(1)
            clear_output()
            display_board(my_board)
            if win_check(my_board,player2):
                print("Player 2 Won!")
                game_on = False
            elif full_board_check(my_board):
                print("Oh! Game tied.")
                game_on = False
            else: 
                x = "Player 1"
            

    if not replay():
        game_on = False
        break