from tictactoe import Game

game = Game

game.prompt_game()

game.display_instructions()

game.register_player_names()

while True:
    game.prompt_player_move()
    if game.game_win == True:
        game.display_win_message()
        break
    elif len(game.moves_remaining) == 0:
        print("Cats game!")

