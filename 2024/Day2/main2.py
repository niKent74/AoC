import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
TEST_INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def safe(nums: list[int]) -> bool:
    if nums[0] > nums[len(nums)-1]:
        direction = -1
    else:
        direction = 1
        
    for nb1, nb2 in zip(nums, nums[1:]):
        if not (1 <= (nb2 - nb1) * direction <= 3):
            return False
            
    else:
        return True


if __name__ == '__main__':
    result = 0
    with open(INPUT_TXT, "rt") as f:
        for line in f:
            report = list(map(int, line.split()))
            if safe(report):
                result += 1
            else:
                for i in range(len(report)):
                    newnums = report[:i] + report[i + 1:]
                    if safe(newnums):
                        result += 1
                        break
                
            
    print(result)