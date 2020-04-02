import random


def random_computer_turn(dict, computer_colour):
    arr = dict.items()
    arr = list(filter(lambda x: x[1] == 'white', arr))
    if len(arr) == 0:
        return dict
    arr = [x[0] for x in arr]
    index = random.randint(0, len(arr) - 1)
    dict[arr[index]] = computer_colour

    return dict


'''
def not_random_computer_turn(dict, turn):
    arr = dict.items() 
    turn_arr = list(filter(lambda x: x[1] == turn, arr))
    if len(turn_arr) == 0:
        print("I'm here")
        white_arr = list(filter(lambda x: x[1] == 'white', arr))
        el = min(white_arr, key=lambda x: x[0][0])
    else:
        neighb_el = max(turn_arr, key=lambda x: x[0][0])[0]
        if dict.get((neighb_el[0] + 2, neighb_el[1])) == 'white':
            el = (neighb_el[0] + 2, neighb_el[1])
    print(el)
'''
