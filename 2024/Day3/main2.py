import os.path
import re


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
TEST_INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input2.txt')

do_nt_expr = re.compile(r"(?:(do|don't)\(\)|mul\((\d+),(\d+)\))")
""" 
    (           parentese normale
    ?:          Match 0 or 1 repetition of the regex.
    (           paranthese normale
    do|don't    do or don't
    )           paranthese normale
    \(          escape paranthese qui est dans le pattern
    \)          escape paranthese qui est dans le pattern
    |           used to specify multiple patterns. For example, P1|P2
    mul         texte dans le pattern
    \(          escape paranthese qui est dans le pattern
    ( \d+ )     \d => matches any digit [0-9]; + => 1 ou plusieurs repetitions
    ,           virgule dans le pattern
    ( \d+ )     \d => matches any digit [0-9]; + => 1 ou plusieurs repetitions
    \)          escape paranthese qui est dans le pattern
    )           paranthese normale
"""

result = 0

if __name__ == '__main__':

    with open(INPUT_TXT, "rt") as f:
        txt = f.read()
        f_list = re.findall(do_nt_expr, txt)
        to_include = True
        for i in f_list:
            if i[0] == "don't":
                to_include = False
            elif i[0] == "do":
                to_include = True
            
            if to_include and i[0] == "":
                int_result = int(i[1]) * int(i[2])
                result += int_result  

    print(result)

