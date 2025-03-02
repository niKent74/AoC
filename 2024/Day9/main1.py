import os.path
import time

start_time = time.time()
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
TEST_INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')


def read_input(filename, sep, type):
    with open(filename, "rt") as f:
        return [list(item) for item in f.read().splitlines()][0]


def calc_checksum(disk):
    nbr = 0
    result = 0
    nb_count = disk.count(".")
    print(len(disk))
    print(nb_count)
    for i in range(0, len(disk) - nb_count):
        result += i * int(disk[i])
        print(f" {i} * {int(disk[i])} = {i * int(disk[i])} -> Global: {result}")
    
    return result


def chg_extend_disk(disk):
    dernier = len(disk) - 1
    nb_count = disk.count(".")
    for n in range(len(disk) - nb_count):
        #print(len(disk[n]))
            
        if disk_blocks[n] == ".":
            while disk_blocks[dernier] == ".":
                dernier -= 1
            str_front_to_back = disk_blocks[n]
            str_back_to_front = disk_blocks[dernier]
            disk.pop(n)
            disk.insert(n, str_back_to_front)
            disk.pop(dernier)
            disk.append(str_front_to_back)   
            dernier -= 1
    return disk

        
def extend_disk(disk):
    disk_blocks = []
    n_bis = 0
    for n in range(len(disk)):
        if n % 2 == 0:
            if disk[n] != "0":
                for i in range(int(disk[n])):
                    disk_blocks.append(str(n_bis))
            else:
                continue
            if n_bis == 9:
                n_bis = 0
            else:
                n_bis += 1
        else:
            if disk[n] != "0":
                for i in range(int(disk[n])):
                    disk_blocks.append(".")
            else:
                continue
    return disk_blocks

        
if __name__ == '__main__':
    puzzle_grid = read_input(TEST_INPUT_TXT, "", "list")
    print("length of the input: " , len(puzzle_grid))
    disk_blocks = extend_disk(puzzle_grid)
    #disk_str = "".join(disk_blocks)
    disk_blocks_new = chg_extend_disk(disk_blocks)
    print(calc_checksum(disk_blocks_new))

print("program ended")

end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
