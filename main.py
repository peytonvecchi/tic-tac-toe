from tictactoe import Game

game = Game

game.prompt_game()

game.display_instructions()

game.register_player_names()

while True:
    game.prompt_player_move()
    game.nothing_going_on_here()
