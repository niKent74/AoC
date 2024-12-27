import os.path
import time

start_time = time.time()
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
TEST_INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')
result = 0
directions =[["^", (-1, 0)], [">", (0, 1)], ["v", (1, 0)], ["<", (0, -1)]]
directions_symbols =["^", ">", "v", "<"]



def read_input(filename, sep, type):
    with open(filename, "rt") as f:
        puzzle  = f.read().splitlines()
        puzzle_grid = [list(item) for item in puzzle]
    return puzzle_grid


def current_pos(puzzle_grid, rows, cols):
    for row in range(rows):
        for col in range(cols):
            if puzzle_grid[row][col] in directions_symbols:
                start_pos_col = col
                start_pos_row = row
                start_symbol = puzzle_grid[row][col]                
                return [start_pos_row, start_pos_col] , start_symbol


def update_position(puzzle_grid, rows, cols, cur_pos, cur_dir):
    if cur_dir == "^":
        r = cur_pos[0] + (-1)
        c = cur_pos[1] + (0)
        if is_valid_position(rows, cols, r, c) == False:
            puzzle_grid[cur_pos[0]][cur_pos[1]] = "X"
            new_dir = "Q"
            new_pos = cur_pos
            return new_pos, new_dir
        else:
            if puzzle_grid[r][c] == "." or puzzle_grid[r][c] == "X":
                new_pos = [r, c]
                new_dir = "^"
                puzzle_grid[r][c] = "^"
                puzzle_grid[cur_pos[0]][cur_pos[1]] = "X"
                return new_pos, new_dir

            elif puzzle_grid[r][c] == "#":
                new_pos = cur_pos
                new_dir = ">"
                return new_pos, new_dir
        
    elif cur_dir == "v":
        r = cur_pos[0] + (1)
        c = cur_pos[1] + (0)
        if is_valid_position(rows, cols, r, c) == False:
            puzzle_grid[cur_pos[0]][cur_pos[1]] = "X"
            new_dir = "Q"
            new_pos = cur_pos
            return new_pos, new_dir
        else:
            if puzzle_grid[r][c] == "." or puzzle_grid[r][c] == "X":
                new_pos = [r, c]
                new_dir = "v"
                puzzle_grid[r][c] = "v"
                puzzle_grid[cur_pos[0]][cur_pos[1]] = "X"
                return new_pos, new_dir
            elif puzzle_grid[r][c] == "#":
                new_pos = cur_pos
                new_dir = "<"
                return new_pos, new_dir
        
    elif cur_dir == ">":
        r = cur_pos[0] + (0)
        c = cur_pos[1] + (1)
        if is_valid_position(rows, cols, r, c) == False:
            puzzle_grid[cur_pos[0]][cur_pos[1]] = "X"
            new_dir = "Q"
            new_pos = cur_pos
            return new_pos, new_dir
        else:
            if puzzle_grid[r][c] == "." or puzzle_grid[r][c] == "X":
                new_pos = [r, c]
                new_dir = ">"
                puzzle_grid[r][c] = ">"
                puzzle_grid[cur_pos[0]][cur_pos[1]] = "X"
                return new_pos, new_dir
            elif puzzle_grid[r][c] == "#":
                new_pos = cur_pos
                new_dir = "v"
                return new_pos, new_dir
    elif cur_dir == "<":
        r = cur_pos[0] + (0)
        c = cur_pos[1] + (-1)
        if is_valid_position(rows, cols, r, c) == False:
            puzzle_grid[cur_pos[0]][cur_pos[1]] = "X"
            new_dir = ""
            new_pos = cur_pos
            return new_pos, new_dir
        else:
            if puzzle_grid[r][c] == "." or puzzle_grid[r][c] == "X":
                new_pos = [r, c]
                new_dir = "<"
                puzzle_grid[r][c] = "<"
                puzzle_grid[cur_pos[0]][cur_pos[1]] = "X"
                return new_pos, new_dir
            elif puzzle_grid[r][c] == "#":
                new_pos = cur_pos
                new_dir = "^"
                return new_pos, new_dir
    else:
        return cur_pos, 'q'


def is_valid_position(rows, cols, r, c):
    if (0 <= r < rows and 0 <= c < cols):
        return True
    else:
        return False


if __name__ == '__main__':
    puzzle_grid = read_input(INPUT_TXT, "", "list")
    rows = len(puzzle_grid)
    cols = len(puzzle_grid[0])
    cur_pos, cur_dir = current_pos(puzzle_grid, rows, cols)
    
    while cur_dir in directions_symbols:
        cur_pos, cur_dir = update_position(puzzle_grid, rows, cols, cur_pos, cur_dir)
    
    for row in range(rows):
        for col in range(cols):
            if puzzle_grid[row][col] == "X":
                result += 1


print(result)
print("program ended")
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))

