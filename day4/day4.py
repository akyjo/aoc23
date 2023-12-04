from pprint import pprint
f = open("day4data.txt", "r")
lines = [line.split(":")[1][1:-1] for line in f.readlines()]

lines = [line.split("|") for line in lines]
lines
pprint(lines)


for line in lines:
    for record in line:
        record = list(map(int, filter(lambda x: len(x) > 0,record.split(" "))))
        print(record)

