# Need two players
from os import system

class Game:
    def __init__(self):
        self.game_go = False
        self.player1_name = ''
        self.player2_name = ''
        self.player1_turn = True
        self.player1_moves = ['', '', ''
                              '', '', ''
                              '', '', '']
        self.game_board = '''
            |    |        
        ____|____|____
            |    | 
        ____|____|____
            |    |
            |    |
'''

    def prompt_game():

        system('clear')
        
        print("Would you like to play a game of tic-tac-toe? (y/n)")
        user_input = input().lower()

        while user_input != 'y' and user_input != 'n' and user_input != 'no' and user_input != 'yes':
            system('clear')
            print("Please enter 'y' or 'n'. Would you like to play a game of tic-tac-toe?")
            user_input = input().lower()
        
        if user_input == 'y' or user_input == 'yes':
            Game.game_go = True
        else:
            print("Okay, perhaps another time :)")
            exit()

    def display_instructions():
        print("\ninstructions: lorem ipsum\n")
        print("press any key to continue...")
        input()

    def register_player_names():
        Game.player1_name = input("Player 1, please enter your name: ")
        Game.player2_name = input("Player 2, please enter your name: ")

    def prompt_player_move():
        
        if Game.player1_turn == True:
            print(f"Okay! {Game.player1_name}, it's your turn! From left to right, enter the number of the space you would like to place an 'X' in.")
            print("Example: to place an 'X' in the middle right space, enter '6'.")


    def print_game_board():
        print(Game.game_board)

        


'''
Flow

1. ask user if they would like to play, let them know they need
another person

2. prompt player1 to enter name and if they want X or O

3. prompt player2 to enter their name and let them know which symbol they are

4. prompt user if they would like instructions on how to play, then print instructions

5. wait for user to press any key to continue

6. flip a coin to see who goes first

'''

