import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'day1-input.txt')

words = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


with open(INPUT_TXT, "rt") as f:
    result = 0
    for line in f.readlines():
        nbr_list = []
        first = ""
        last = ""
        for i in range(len(line.strip())):
            c = line[i]
            l = line[i:].strip()
            if c.isdigit():
                nbr_list.append(c)
                
                
            if c.isalpha():
                for j, word in enumerate(words):
                    if l.startswith(word):
                        nbr_list.append(str(j))
        result += int(nbr_list[0]+nbr_list[-1])
                    

    print(result)
    