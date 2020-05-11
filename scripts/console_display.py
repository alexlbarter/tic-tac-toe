def generate_display_str(game_state, symbols=(" ", "O", "X")):
    chars = [symbols[x] for x in game_state]
    output = [f" {chars[0]} | {chars[1]} | {chars[2]} ", "---+---+---", f" {chars[3]} | {chars[4]} | {chars[5]} ",
              "---+---+---", f" {chars[6]} | {chars[7]} | {chars[8]} "]

    return "\n".join(output)


def display_game(game_state, symbols=(" ", "O", "X")):
    for symbol in symbols:
        if len(symbol) != 1:
            raise ValueError(f"Custom player symbols must have length of 1, not {len(symbol)}")
    if symbols[1] == symbols[2]:
        raise ValueError(f"Player symbols must be unique, both were {symbols[1]}")
    print("\n\n", generate_display_str(game_state, symbols), sep="")
