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
            # game_state uses indexes 0-8 internally, but to the user they are numbered 1-9 from the top left
            # get_move() will automatically convert the number from the user's perspective to the correct index

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
                        return names.index(name)
                else:
                    raise ValueError("Not a valid position")
            else:
                if 1 <= move <= 9:
                    return move - 1
                else:
                    raise ValueError("Not a valid position")

    def set_move(self, player, move):
        if self.game_state[move] == 0:
            self.game_state[move] = player
        else:
            raise ValueError("Position already occupied")

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
        # while there are still empty spaces
        while 0 in self.game_state:
            if self.mode == "console":
                console_display.display_game(self.game_state, self.symbols)
            player_turn = next(player_turn_gen)
            if player_turn == 1:
                while True:
                    try:
                        self.set_move(1, self.get_move())
                    except ValueError:
                        pass
                    else:
                        break
            elif player_turn == 2:
                if self.num_players == 1:
                    self.set_move(2, self.com_move())
                elif self.num_players == 2:
                    self.set_move(2, self.get_move())
            winner = self.check_winner()
            if winner is not None:
                print(f"Player {winner} wins!")
                break

    def com_move(self):
        # -- Offence
        # Find a line with one gap and two of its own moves
        for line in self.LINES:
            game_line = [self.game_state[x] for x in line]
            if game_line.count(2) == 2 and game_line.count(0) == 1:
                com_move = line[game_line.index(0)]
                return com_move

        # -- Defence
        # Find a line with one gap and two of opponent's moves
        for line in self.LINES:
            game_line = [self.game_state[x] for x in line]
            if game_line.count(1) == 2 and game_line.count(0) == 1:
                com_move = line[game_line.index(0)]
                return com_move

        # -- Else random
        # If com player isn't about to win or lose, pick a random space which is still empty
        while True:
            com_move = random.randint(1, 9)
            if self.game_state[com_move] == 0:
                return com_move


if __name__ == "__main__":
    players = int(input("How many players? ").strip())
    game = Game(players)
    game.play()
