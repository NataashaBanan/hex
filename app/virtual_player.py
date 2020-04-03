import random
from collections import deque

from app.turn_and_color import Color


def color_element(game, key):
    game.hex_dictionary[key] = game.turn.color
    game.undo_history.append((key, game.turn.color))


def random_computer_turn(game):
    arr = game.hex_dictionary.items()
    arr = list(filter(lambda x: x[1] == Color.White, arr))
    arr = [x[0] for x in arr]
    index = random.randint(0, len(arr) - 1)
    color_element(game, arr[index])

    return game.hex_dictionary


def smart_computer_turn(game):
    arr = game.hex_dictionary.items()
    arr = list(filter(lambda el: el[1] == game.turn.color, arr))
    # смотрю все ячейки цвета виртуального игрока

    if len(arr) == 0:  # если таких ещё неть
        x = 1 - game.rang
        y = (game.rang - 1) * 2
        if game.hex_dictionary[(x, y)] == Color.White:
            # пытаемся закрасить левый угол
            color_element(game, (x, y))
            return
        color_element(game, (x + 1, y - 2))
        # красим тот который сверху справа
        return

    previous = max(arr, key=lambda el: el[0][0])
    # смотрим самый правый данного цвета

    x = previous[0][0]
    y = previous[0][1]

    if y == (game.rang - 1) * 4 - 2 * x:
        random_computer_turn(game)
        return

    if game.hex_dictionary.get((x + 2, y)) == Color.White:
        color_element(game, (x + 2, y))
        return

    if game.hex_dictionary.get((x + 1, y + 2)) == Color.White:
        color_element(game, (x + 1, y + 2))
        return

    if game.hex_dictionary.get((x + 1, y - 2)) == Color.White:
        color_element(game, (x + 1, y - 2))
        return

    random_computer_turn(game)
