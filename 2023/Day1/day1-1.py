import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'day1-input.txt')

number = 0
total = 0

with open(INPUT_TXT, "rt") as f:
    lines = f.readlines()
    for line in lines:
        numbers = []
        for ch in line:
            if ch.isdigit():
                numbers.append(ch)
        number = int(numbers[0]+numbers[-1])
        total += number
    print(total)

