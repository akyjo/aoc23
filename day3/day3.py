import re
f = open("day3_data.txt", "r")
lines = f.readlines()
indices, sum = [], 0
filelen = len(lines)

for i,line in enumerate(lines):

    for match in re.finditer(r'\d+', line):
        # [ číslo řádku, číslo ze stringu, zač. ind, konc. ind ]
        indices.append( [i, int(match.group()), match.start(), match.end() -1] )

def contains_symbol(line, start, end):

    for c in line[start:end + 1]:

        if not c.isdigit() and c != '.' and c != '\n':
            return True

    return False

for rec in indices:

    for line in lines[max(0, rec[0] - 1): min(filelen, rec[0] + 1) + 1]:
        linelen = len(line)

        if contains_symbol(line, max(0, rec[2] - 1), min(linelen, rec[3] + 1)):
            sum += rec[1]
            break

print(sum)
