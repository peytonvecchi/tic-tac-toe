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
    player1_win_track = []
    game_win = False

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
                print("Cannot put character here, try again (Press Enter to continue)")
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
                print("Cannot put character here, try again (Press Enter to continue)")
                input()
        Game.check_winner()

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

    def display_win_message():
        system('clear')
        if Game.player1_turn == False:
            print(f'{Game.player1_name} wins!!')
        else:
            print(f'{Game.player2_name} wins!!')
        Game.print_game_board()

    def check_winner():
        if Game.player_moves[0] == 'X' and Game.player_moves[3] == 'X' and Game.player_moves[6] == 'X':
            Game.game_win = True
        elif Game.player_moves[1] == 'X' and Game.player_moves[4] == 'X' and Game.player_moves[7] == 'X':
            Game.game_win = True
        elif Game.player_moves[2] == 'X' and Game.player_moves[5] == 'X' and Game.player_moves[8] == 'X':
            Game.game_win = True
        elif Game.player_moves[0] == 'X' and Game.player_moves[1] == 'X' and Game.player_moves[2] == 'X':
            Game.game_win = True
        elif Game.player_moves[3] == 'X' and Game.player_moves[4] == 'X' and Game.player_moves[5] == 'X':
            Game.game_win = True
        elif Game.player_moves[6] == 'X' and Game.player_moves[7] == 'X' and Game.player_moves[8] == 'X':
            Game.game_win = True
        elif Game.player_moves[0] == 'X' and Game.player_moves[4] == 'X' and Game.player_moves[8] == 'X':
            Game.game_win = True
        elif Game.player_moves[6] == 'X' and Game.player_moves[4] == 'X' and Game.player_moves[2] == 'X':
            Game.game_win = True
        elif Game.player_moves[0] == 'O' and Game.player_moves[3] == 'O' and Game.player_moves[6] == 'O':
            Game.game_win = True
        elif Game.player_moves[1] == 'O' and Game.player_moves[4] == 'O' and Game.player_moves[7] == 'O':
            Game.game_win = True
        elif Game.player_moves[2] == 'O' and Game.player_moves[5] == 'O' and Game.player_moves[8] == 'O':
            Game.game_win = True
        elif Game.player_moves[0] == 'O' and Game.player_moves[1] == 'O' and Game.player_moves[2] == 'O':
            Game.game_win = True
        elif Game.player_moves[3] == 'O' and Game.player_moves[4] == 'O' and Game.player_moves[5] == 'O':
            Game.game_win = True
        elif Game.player_moves[6] == 'O' and Game.player_moves[7] == 'O' and Game.player_moves[8] == 'O':
           Game.game_win = True
        elif Game.player_moves[0] == 'O' and Game.player_moves[4] == 'O' and Game.player_moves[8] == 'O':
            Game.game_win = True
        elif Game.player_moves[6] == 'O' and Game.player_moves[4] == 'O' and Game.player_moves[2] == 'O':
            Game.game_win = True


