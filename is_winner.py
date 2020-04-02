from collections import deque


def is_winner(dictionary, turn, field_rang):

    q = deque()

    # если был ход красного запускаем обход в ширину от верхней правой стороны
    if turn == 'red':
        for k in range(0, field_rang):
            if dictionary[(k, k * 2)] == turn:
                q.append((k, k * 2))
    #  и наоборот от верхней левой
    if turn == 'blue':
        for k in range(0, field_rang):
            if dictionary[(-k, k * 2)] == turn:
                q.append((-k, k * 2))

    # if len(q) == 0:
    #   return False

    return make_seq(dictionary, turn, [], field_rang, q)


def make_seq(dictionary, turn, visited, field_rang, queue):
    while len(queue) > 0:
        point = queue.pop()
        x = point[0]
        y = point[1]
        visited.append(point)
        # проверяем, что дошли до противоположной стороны
        if turn == 'red' and x * 2 + 4 * (field_rang - 1) == y:
            return True
        if turn == 'blue' and x * (-2) + 4 * (field_rang - 1) == y:
            return True
        all_concerning = [(x - 2, y), (x + 2, y), (x - 1, y - 2),
                          (x + 1, y - 2), (x - 1, y + 2), (x + 1, y + 2)]
        # добавляем все соседние ячейки нужного цвета
        # которые ещё не были посещены
        for i in all_concerning:
            if i not in visited and dictionary.get(i) == turn:
                queue.append(i)
    return False
