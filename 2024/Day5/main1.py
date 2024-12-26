import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
RULES_TXT = os.path.join(os.path.dirname(__file__), 'rules.txt')
TEST_INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')
TEST_RULES_TXT = os.path.join(os.path.dirname(__file__), 'test_rules.txt')
result = 0

def read_input(filename, sep, type):
    with open(filename, "rt") as f:
        puzzle  = f.read().splitlines()
    if type == "list":
        puzzle_grid = [list(item.split(sep)) for item in puzzle]
    elif type == "tuple":
        puzzle_grid = [tuple(item.split(sep)) for item in puzzle]
    return puzzle_grid

    
def check_update(page):
    for i in range(len(page)):
        page_cur = page[i]
        page_before = page[:i]
        page_after = page[i+1:]
        if not check_rules(rules, page_cur, page_before, page_after):
            return False
    print(page[len(page)//2+1])
    return int(page[len(page)//2+1])



def check_rules(rules, page_cur, page_before, page_after):
    for a,b in rules:
        if a == page_cur:
            b_count = page_after.count(b)
            b_check = b not in page_before
            if b_count >= 0 and b_check:
                print("check ok")
                
            else:
                print("not ok")
                return False
        
        if b == page_cur:
            a_count = page_before.count(a)
            a_check = a not in page_after
            if a_count >=0 and a_check:
                print("check ok")
                
            else:
                print("not ok")
                return False

    return True


if __name__ == '__main__':
    pages = read_input(TEST_INPUT_TXT, ",", "list")
    rules = read_input(TEST_RULES_TXT, "|", "tuple")
    for i in range(len(pages)):
        result += check_update(pages[i])
        print(result)


print(result)
print("program ended")
