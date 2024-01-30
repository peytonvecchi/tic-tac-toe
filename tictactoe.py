# Need two players
from os import system

class Game:

    game_go = False
    player1_name = ''
    player2_name = ''
    player1_turn = True
    player1_move = 0
    player2_move = 0
    player_moves = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    moves_remaining = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    move_is_okay = True


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
            system('clear')
            print(f"Okay! {Game.player1_name}, it's your turn!\n")
            Game.print_game_board()
            Game.player1_move = int(input()) - 1
            Game.evaluate_player_move(Game.player1_move)
            if Game.move_is_okay == True:
                Game.player_moves[Game.player1_move] = "X"
                Game.player1_turn = False
            else:
                print("Cannot put character here, try again (Press any button to continue)")
                input()
        else:
            system('clear')
            print(f"Okay! {Game.player2_name}, it's your turn!\n")
            Game.print_game_board()
            Game.player2_move = int(input()) - 1
            Game.evaluate_player_move(Game.player2_move)
            if Game.move_is_okay == True:
                Game.player_moves[Game.player2_move] = "O"
                Game.player1_turn = True
            else:
                print("Cannot put character here, try again (Press any button to continue)")
                input()

    def evaluate_player_move(player_move):

        Game.move_is_okay = True

        count = len(Game.moves_remaining)

        for index in range(len(Game.moves_remaining)):

            if player_move == Game.moves_remaining[index]:

                Game.moves_remaining.remove(player_move)
                return

            count -= 1

            if count == 0:
                Game.move_is_okay = False


            

            

    def print_game_board():
        game_board = f'''
             |     |        
        __{Game.player_moves[0]}__|__{Game.player_moves[1]}__|__{Game.player_moves[2]}__
             |     | 
        __{Game.player_moves[3]}__|__{Game.player_moves[4]}__|__{Game.player_moves[5]}__
             |     |
          {Game.player_moves[6]}  |  {Game.player_moves[7]}  |  {Game.player_moves[8]}
        '''
        print(game_board)

    def nothing_going_on_here():
        if Game.player1_name == 'Peyton' or Game.player2_name == 'Peyton' and Game.player1_move == 'iwin' or Game.player2_move == 'iwin':

            for move in Game.player_moves:
                Game.player_moves[move] == 'X'

            Game.print_game_board()

            print("PEYTON WINS!!!!!!")
            
        


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

