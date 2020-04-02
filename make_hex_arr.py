
def make_hex_dict(n):
    dictionary = {}

    for count in range(0, n):
        if count % 2 == 0:
            for i in range(count // -2, count // 2 + 1):
                dictionary[(i * 2, 2 * count)] = 'white'
        else:
            for i in range(0, count + 1):
                dictionary[(- count + i * 2, 2 * count)] = 'white'
    for count in range(0, n - 1):
        if count % 2 == 0:
            for i in range(-count // 2, count // 2 + 1):
                dictionary[(i * 2, 2 * (n - 1) + (n - 1 - count) * 2)] =\
                    'white'
        else:
            for i in range(0, count + 1):
                dictionary[(-count + i * 2,
                            2 * (n - 1) + (n - 1 - count) * 2)] = 'white'

    return dictionary
