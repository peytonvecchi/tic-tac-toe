# Need two players

class Game:
    def __init__(self):
        self.game_go = False

    def prompt_game():
        
        print("Would you like to play a game of tic-tac-toe? (y/n)")
        user_input = input().lower()

        while user_input != 'y' and user_input != 'n' and user_input != 'no' and user_input != 'yes':
            print("Please enter 'y' or 'n'.")
            user_input = input().lower()


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
