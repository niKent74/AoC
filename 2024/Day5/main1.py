import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
RULES_TXT = os.path.join(os.path.dirname(__file__), 'rules.txt')
TEST_INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')
TEST_RULES_TXT = os.path.join(os.path.dirname(__file__), 'test_rules.txt')


def read_input(filename):
    with open(filename, "rt") as f:
        puzzle  = f.read().strip(",").splitlines()

    puzzle_grid = [list(row) for row in puzzle]
    return puzzle_grid




if __name__ == '__main__':
    puzzle = read_input(TEST_INPUT_TXT)
    rules = read_input(TEST_RULES_TXT)


print("program ended")
