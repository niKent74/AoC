import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
TEST_INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')


def read_input(filename):
    with open(filename, "rt") as f:
        puzzle  = f.read().strip().splitlines()

    puzzle_grid = [list(row) for row in puzzle]
    return puzzle_grid


def is_valid_direction(target_length, rows, cols, row, col, dr, dc):
    for i in range(target_length):
        r = row + i * dr
        c = col + i * dc
        if not (0 <= r < rows and 0 <= c < cols) or puzzle_grid[r][c] != keyword[i]:
            return False
    return True


def xmas_search(puzzle_grid, keyword):
    target_length = len(keyword)
    count = 0
    rows = len(puzzle_grid)
    cols = len(puzzle_grid[0])
    for row in range(rows):
        for col in range(cols):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
            for dr, dc in directions:
                if is_valid_direction(target_length, rows, cols, row, col, dr, dc):
                    count += 1

    return count


if __name__ == '__main__':
    keyword = "XMAS"
    puzzle_grid = read_input(INPUT_TXT)
    print(xmas_search(puzzle_grid, keyword))



print("program ended")
