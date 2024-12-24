import os.path
import re


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
TEST_INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

# epreuve = re.compile(r'mul\(\d+,\d+\)')
epreuve = re.compile(r'mul\((\d+),(\d+)\)')
""" mul         texte dans le pattern
    \(          escape paranthese qui est dans le pattern
    ( \d+ )     \d => matches any digit [0-9]; + => 1 ou plusieurs repetitions
    ,           virgule dans le pattern
    ( \d+ )     \d => matches any digit [0-9]; + => 1 ou plusieurs repetitions
    \)          escape paranthese qui est dans le pattern

"""
result = 0


if __name__ == '__main__':

    with open(INPUT_TXT, "rt") as f:
        txt = f.read()
        f_list = re.findall(epreuve, txt)
        for i in f_list:
            int_result = int(i[0]) * int(i[1])
            result += int_result

    print(result)

