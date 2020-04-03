from collections import deque

from app.turn_and_color import Color


def is_winner(game):
    q = deque()

    # если был ход красного запускаем обход в ширину
    # от верхней правой стороны
    if game.turn.color == Color.Red:
        for k in range(0, game.rang):
            if game.hex_dictionary[(k, k * 2)] == game.turn.color:
                q.append((k, k * 2))
    #  и наоборот от верхней левой
    if game.turn.color == Color.Blue:
        for k in range(0, game.rang):
            if game.hex_dictionary[(-k, k * 2)] == game.turn.color:
                q.append((-k, k * 2))

    # if len(q) == 0:
    #   return False

    return make_seq(game, [], q)


def make_seq(game, visited, queue):
    while len(queue) > 0:
        point = queue.pop()
        x = point[0]
        y = point[1]
        visited.append(point)
        # проверяем, что дошли до противоположной стороны
        if game.turn.color == Color.Red and \
                x * 2 + 4 * (game.rang - 1) == y:
            return True
        if game.turn.color == Color.Blue and \
                x * (-2) + 4 * (game.rang - 1) == y:
            return True
        all_concerning = [(x - 2, y), (x + 2, y), (x - 1, y - 2),
                          (x + 1, y - 2), (x - 1, y + 2),
                          (x + 1, y + 2)]
        # добавляем все соседние ячейки нужного цвета
        # которые ещё не были посещены
        for i in all_concerning:
            if i not in visited and \
                    game.hex_dictionary.get(i) == game.turn.color:
                queue.append(i)
    return False
