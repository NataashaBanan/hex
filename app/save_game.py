from app.turn_and_color import Turn, Color
from app.difficulty import Difficulty

import os


def save(string, game):
    path = os.path.join(os.getcwd(), 'saves', string + '.txt')

    try:
        file = open(path, 'r')
        file.close()
    except FileNotFoundError:
        file = open(path, 'w')
        file.close()

    with open(path, 'w') as f:
        f.write(str(game.turn) + '\n')
        f.write(str(game.hot_seat) + '\n')
        f.write(str(game.difficult) + '\n')
        f.write(str(game.rang) + '\n')
        for i in game.hex_dictionary.values():
            f.write(str(i) + '\n')


def print_saves(painter, n):
    a = 0
    for line in get_saves():
        painter.drawText(100, 200 + a * 50, line)
        a += 1

    mark(painter, n)


def mark(painter, n):
    if len(get_saves()) == 0:
        return
    painter.drawText(102, 200 + n * 50, get_saves()[n])


def get_saves():
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(os.path.join(os.getcwd(), "saves")):
        for file in f:
            if '.txt' in file:
                files.append(str(file)[:-4])

    return files


def load(game, n):
    if len(get_saves()) == 0:
        return
    with open(os.path.join(os.getcwd(), 'saves', get_saves()[n] + '.txt'),
              'r') as f:
        text = f.read()
    ar = text.split('\n')

    game.rang = int(ar[3])
    game.new_game()

    if ar[0] == 'Red':
        game.turn = Turn(Color.Red)
    elif ar[0] == 'Blue':
        game.turn = Turn(Color.Blue)
    else:
        raise RuntimeError

    if ar[1] == 'False':
        game.hot_seat = False
    elif ar[1] == 'True':
        game.hot_seat = True
    else:
        raise RuntimeError

    if ar[2] == str(Difficulty.easy):
        game.difficult = Difficulty.easy
    elif ar[2] == str(Difficulty.hard):
        game.difficult = Difficulty.hard
    else:
        raise RuntimeError

    keys = list(game.hex_dictionary.keys())

    for j in range(4, len(ar)):
        if ar[j] == str(Color.Blue):
            c = Color.Blue
        elif ar[j] == str(Color.Red):
            c = Color.Red
        elif ar[j] == str(Color.White):
            c = Color.White
        else:
            break

        game.hex_dictionary[keys[j - 4]] = c
