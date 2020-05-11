from scripts import console_display
import random
from itertools import cycle


class Game:
    DEFAULT_SYMBOLS = (" ", "O", "X")
    LINES = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

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
            move = input("Move: ").strip().lower()
            try:
                move = int(move)
            except ValueError:
                names = [["top left", "left top"],
                         ["top middle", "middle top"],
                         ["top right", "right top"],
                         ["middle left", "left middle"],
                         ["centre", "center", "middle"],
                         ["middle right", "right middle"],
                         ["bottom left", "left bottom"],
                         ["bottom middle", "middle bottom"],
                         ["bottom right", "right bottom"]]
                for name in names:
                    if move in name:
                        return names.index(name) + 1
                else:
                    raise ValueError("Not a valid position")
            else:
                if 1 <= move <= 9:
                    return move
                else:
                    raise ValueError("Not a valid position")

    def set_move(self, player, move):
        self.game_state[move - 1] = player

    def check_winner(self):
        for line in self.LINES:
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
            # while there are still empty spaces
            while 0 in self.game_state:
                if self.mode == "console":
                    console_display.display_game(self.game_state, self.symbols)
                player_turn = next(player_turn_gen)
                if player_turn == 1:
                    self.set_move(1, self.get_move())
                elif player_turn == 2:
                    self.com_move()
                winner = self.check_winner()
                if winner is not None:
                    print(f"Player {winner} wins!")
                    break

        elif self.num_players == 2:
            pass

    def com_move(self):
        # TODO: implement smart AI, not just random moves
        # -- Offence
        # Find a line with one gap
        for line in self.LINES:
            game_line = [self.game_state[x] for x in line]
            if game_line.count(2) == 2 and game_line.count(0) == 1:
                com_move = line[game_line.index(0)]
                game.set_move(2, com_move)


if __name__ == "__main__":
    game = Game(1)
    game.play()
