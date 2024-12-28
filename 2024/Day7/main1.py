import os.path
import time

start_time = time.time()
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
TEST_INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')


def read_input(filename, sep, type):
    with open(filename, "rt") as f:
        return [
            [int(item.split(": ")[0]), [int(x) if x.isdigit() else x for x in item.split(": ")[1].split()]]
            for item in f.read().splitlines()
        ]


def check_calc(result, numbers):
    if len(numbers) == 1:
        return result == numbers[0]
    first, second = numbers[:2]
    sum_result = first + second
    mul_result = first * second  
    return check_calc(result, [sum_result, *numbers[2:]]) or check_calc(result, [mul_result, *numbers[2:]])
        

if __name__ == '__main__':
    puzzle_grid = read_input(INPUT_TXT, "", "list")
    good = []
    for i in range(len(puzzle_grid)):
        if check_calc(puzzle_grid[i][0], puzzle_grid[i][1]):
            good.append(puzzle_grid[i][0])


print(sum(good))
print("program ended")
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
