import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
TEST_INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')


def read_input(filename):
    with open(filename, "rt") as f:
        puzzle  = f.read().strip().splitlines()

    puzzle_grid = [list(row) for row in puzzle]
    return puzzle_grid


def is_valid_direction(rows, cols, row, col, directions):
    result = []
    for dr, dc in directions:
        r = row + dr
        c = col + dc
        if (0 <= r < rows and 0 <= c < cols):
            result.append(True)
        elif not (0 <= r < rows and 0 <= c < cols):
            result.append(False)
        else:
            result.append(False)

    if result.count(True) == 4:
        return True
    else:
        return False


def mas_search(puzzle_grid):
    
    directions = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
    count = 0
    rows = len(puzzle_grid)
    cols = len(puzzle_grid[0])
    for row in range(rows):
        for col in range(cols):
            cur_pos = puzzle_grid[row][col]
            if cur_pos == "A":
                if is_valid_direction(rows, cols, row, col, directions) == False:
                    continue
                if puzzle_grid[row][col] == "A" and puzzle_grid[row-1][col-1] == "M" and puzzle_grid[row+1][col+1] == "S" or puzzle_grid[row][col] == "A" and puzzle_grid[row-1][col-1] == "S" and puzzle_grid[row+1][col+1] == "M":
                    if puzzle_grid[row][col] == "A" and puzzle_grid[row-1][col+1] == "M" and puzzle_grid[row+1][col-1] == "S" or puzzle_grid[row][col] == "A" and puzzle_grid[row-1][col+1] == "S" and puzzle_grid[row+1][col-1] == "M":
                        count += 1
                    
    return count


if __name__ == '__main__':
    keyword = "MAS"
    puzzle_grid = read_input(INPUT_TXT)
    print(mas_search(puzzle_grid))


print("program ended")
