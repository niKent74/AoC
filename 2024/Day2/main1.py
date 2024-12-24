import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
TEST_INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def safe(nums: list[int]) -> bool:
    if report[0] > report[len(report)-1]:
        direction = -1
    else:
        direction = 1
        
    for nb1, nb2 in zip(report, report[1:]):
        if not (1 <= (nb2 - nb1) * direction <= 3):
            return False
            
    else:
        return True


if __name__ == '__main__':
    result = 0
    with open(INPUT_TXT, "rt") as f:
        for line in f:
            report = list(map(int, line.split()))
            is_safe = safe(report)
            if is_safe:
                result += 1
            
    print(result)