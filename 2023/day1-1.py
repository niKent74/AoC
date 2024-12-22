
number = 0
total = 0

with open("day1-input.txt", "rt") as f:
    lines = f.readlines()
    for line in lines:
        numbers = []
        for ch in line:
            if ch.isdigit():
                numbers.append(ch)
        number = int(numbers[0]+numbers[-1])
        total += number
    print(total)

