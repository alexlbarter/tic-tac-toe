from scripts import console_display
import random
from itertools import cycle


class Game:
    DEFAULT_SYMBOLS = (" ", "O", "X")

    def __init__(self, num_players, mode="console", custom_symbols=None):
        self.num_players = num_players
        self.mode = mode
        if custom_symbols:
            self.symbols = custom_symbols
        else:
            self.symbols = self.DEFAULT_SYMBOLS
        self.game_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def get_move(self):
        if self.mode == "console":
            # numbered 1-9 from top left across
            # TODO: update to allow move in words, i.e. 'top left' or 'middle right'
            move = int(input("Move: ").strip())
            return move

    def set_move(self, player, move):
        self.game_state[move - 1] = player

    def check_winner(self):
        lines = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for line in lines:
            if self.game_state[line[0]] == self.game_state[line[1]] == self.game_state[line[2]]:
                if self.game_state[line[0]] == 0:
                    continue
                else:
                    return self.game_state[line[0]]
        else:
            return None

    def play(self):
        player_turn_gen = cycle((1, 2))
        if self.num_players == 1:
            while 0 in self.game_state:
                if self.mode == "console":
                    console_display.display_game(self.game_state, self.symbols)
                # while there are still empty spaces
                player_turn = next(player_turn_gen)
                if player_turn == 1:
                    self.set_move(1, self.get_move())
                elif player_turn == 2:
                    # TODO: implement smart AI, not just random moves
                    while True:
                        com_move = random.randint(1, 9)
                        if self.game_state[com_move - 1] == 0:
                            break
                    self.set_move(2, com_move)

                winner = self.check_winner()
                if winner is not None:
                    print(f"Player {winner} wins!")
                    break

        elif self.num_players == 2:
            pass


if __name__ == "__main__":
    game = Game(1)
    game.play()