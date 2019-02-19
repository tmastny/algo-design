import functools




def compare_color(a, b):
    assert a in ('red', 'blue', 'yellow')
    assert b in ('red', 'blue', 'yellow')

    if a == b:
        return 0

    if b == 'yellow':
        return 1

    if a == 'yellow':
        return -1

    if b == 'blue':
        return 1

    if a == 'blue':
        return -1

    if b == 'red':
        return 1

    if a == 'red':
        return -1




def sort_pairs(pairs):
    colors = {'red' : [], 'blue' : [], 'yellow' : []}
    for pair in pairs:
        colors[pair[1]].append(pair)

    return colors['red'] + colors['blue'] + colors['yellow']



def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


if __name__ == "__main__":
    test_pairs = [(1,'blue'), (3,'red'), (4,'blue'), (6,'yellow'), (9,'red')]

    print(sort_pairs(test_pairs))
