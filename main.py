from tictactoe import Game

game = Game

game.prompt_game()

game.display_instructions()

game.register_player_names()

while True:
    game.player_move()
