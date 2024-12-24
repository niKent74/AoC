import os.path
from collections import defaultdict

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'day2-input.txt')

f = open(INPUT_TXT, "rt").read().strip()

DIC_max = {'red': 12, 'blue': 14, 'green': 13}
DIC = defaultdict(int)
answer = 0
for line in f.splitlines():
    valid = True
    idf, line = line.split(":")
    for tirage in line.split(";"):
        for boules in tirage.split(","):
            nbr, couleur = boules.split()
            if int(nbr) > DIC_max[couleur]:
                valid = False
    if valid:
        answer += int(idf.split()[1])
                
print(answer)
            

        
    

