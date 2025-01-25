import os.path
import time

start_time = time.time()
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
TEST_INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')


def read_input(filename, sep, type):
    with open(filename, "rt") as f:
        return [list(item) for item in f.read().splitlines()]


def antenas(puzzle_grid):
    antenas_loc = []
    antenas_typ = []
    rows = len(puzzle_grid)
    cols = len(puzzle_grid[0])
    for row in range(rows):
        for col in range(cols):
            if puzzle_grid[row][col] != ".":
                antenas_loc.append([puzzle_grid[row][col], (row, col)])
                if puzzle_grid[row][col] not in antenas_typ:
                    antenas_typ.append(puzzle_grid[row][col])
    return antenas_loc, antenas_typ

def antinodes(puzzle_grid, antenas_loc, antenas_typ):
    antinodes_lst = []
    for i in range(len(antenas_loc)):
        antenas_loc_bis = antenas_loc[i+1:]
        for j in range(len(antenas_loc_bis)):
            if antenas_loc[i][0] == antenas_loc_bis[j][0]:
                loc1 = antenas_loc[i][1]
                loc1_num = antenas_loc[i][1][0] * 10 + antenas_loc[i][1][1]
                loc2 = antenas_loc_bis[j][1]
                loc2_num = antenas_loc_bis[j][1][0] * 10 + antenas_loc_bis[j][1][1]
                loc1_r = loc1[0]
                loc1_c = loc1[1]
                loc2_r = loc2[0]
                loc2_c = loc2[1]

                r_diff = loc2_r - loc1_r
                c_diff = loc2_c - loc1_c
                if 0 <= (loc1_r - r_diff) < len(puzzle_grid) and 0 <= (loc1_c - c_diff) < len(puzzle_grid[0]):
                    if [(loc1_r - r_diff, loc1_c - c_diff)] not in antinodes_lst:
                        antinodes_lst.append([(loc1_r - r_diff, loc1_c - c_diff)])
                if 0 <= (loc2_r + r_diff) < len(puzzle_grid) and 0 <= (loc2_c + c_diff) < len(puzzle_grid[0]):
                    if [(loc2_r + r_diff, loc2_c + c_diff)] not in antinodes_lst:
                        antinodes_lst.append([(loc2_r + r_diff, loc2_c + c_diff)])          
                
    return antinodes_lst

        
if __name__ == '__main__':
    puzzle_grid = read_input(TEST_INPUT_TXT, "", "list")
    antenas_loc, antenas_typ = antenas(puzzle_grid)
    antinodes_lst = antinodes(puzzle_grid, antenas_loc, antenas_typ)


print(len(antinodes_lst))
print("program ended")

end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
