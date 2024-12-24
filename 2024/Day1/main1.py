import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def tests():
    list_left = [3, 4, 2, 1, 3, 3]
    list_right = [4, 3, 5, 3, 9, 3]
    list_right.sort()
    list_left.sort()
    assert calc_diff(list_left, list_right) == 11
    

def calc_diff(lst_left, lst_right):
    result = 0
    for l, r in zip(lst_left, lst_right):
        print(l, " - ", r, " = ", abs(int(l) - int(r)))
        result = result + abs(int(l) - int(r))
    return result


def load_input(INPUT_TXT):
    list_left, list_right = [], []
    with open(INPUT_TXT, "rt") as f:
        for line in f:
            list_left.append(line[:5])
            list_right.append(line[8:13])
    list_right.sort()
    list_left.sort()
    return list_left, list_right

if __name__ == '__main__':
    tests()
    list_left, list_right = load_input(INPUT_TXT)
    print(calc_diff(list_left, list_right))
    
    