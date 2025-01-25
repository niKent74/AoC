import os.path
import time

start_time = time.time()
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
TEST_INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')


def read_input(filename, sep, type):
    with open(filename, "rt") as f:
        return [list(item) for item in f.read().splitlines()]



        
if __name__ == '__main__':
    puzzle_grid = read_input(TEST_INPUT_TXT, "", "list")


print(len(antinodes_lst))
print("program ended")

end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
