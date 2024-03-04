DATA_S = """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
        """

result = 0
result_check = 4361

lines = DATA_S.strip().split()
r = len(lines)
c = len(lines[0])


def is_symbol(i, j):
    if ((0 <= i < r) and (0 <= j < c)):
        if lines[i][j] != "." or lines[i][j].isdigit():
            return True
        
    return False


for i,line in enumerate(lines):
    for j,row in enumerate(line):
        print(j)
