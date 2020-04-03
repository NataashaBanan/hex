def check_records():
    try:
        file = open('records.txt', 'r')
        file.close()
    except FileNotFoundError:
        file = open('records.txt', 'w')
        file.close()


def add_new_record(string):
    check_records()

    di = {}
    with open('records.txt', 'r') as file:
        for line in file:
            name, count = line.split()
            di[name] = count

    if di.get(string) is None:
        with open('records.txt', 'a') as file:
            file.write(string + ' 1\n')
    else:
        a = int(di[string])
        a += 1
        di[string] = str(a)
        with open('records.txt', 'w') as file:
            for key in di.keys():
                file.write(key + ' ' + di[key] + '\n')


def get_records():
    check_records()

    result = []
    with open('records.txt', 'r') as file:
        for line in file:
            result.append(line[:-1])
    return result


def print_records(painter):

    painter.drawText(200, 100, "Records")

    x = 0
    for line in get_records():
        res = str(x + 1) + ". " + line
        painter.drawText(200, 150 + 50 * x, res)
        x += 1
