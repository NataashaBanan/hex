from is_winner import is_winner


def update_dict(x, y, dictionary, turn, x0, y0, hex_a):
    new_turn = turn

    for i in dictionary.keys():
        if dictionary[i] != 'white':
            continue
        this_x0 = x0 + i[0] * hex_a
        this_y0 = y0 + i[1] * hex_a
        if x <= this_x0 or y <= this_y0 or x >= this_x0 + hex_a * 2\
                or y >= this_y0 + 3 * hex_a:
            continue
        if y <= this_y0 + hex_a + this_x0 - x:
            continue
        if y >= this_y0 + this_x0 + 4 * hex_a - x:
            continue
        if y >= this_y0 + 2 * hex_a + x - this_x0:
            continue
        if y <= this_y0 - hex_a + x - this_x0:
            continue
        dictionary[i] = turn
        if turn == 'red':
            new_turn = 'blue'
        else:
            new_turn = 'red'

    return dictionary, new_turn


def update_field(x, y, hex_dict, turn, field_rang, x0, y0, hex_a):

    hex_dict, new_turn = update_dict(x, y, hex_dict, turn, x0, y0, hex_a)
    win = False

    if is_winner(hex_dict, turn, field_rang):
        win = True

    return hex_dict, new_turn, win
