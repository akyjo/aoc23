from functools import reduce
f = open("6.txt", "r")
lines = f.readlines()
lines = [ line.split(':')[1].strip() for line in lines]
lines = [ [int(x) for x in line.split()] for line in lines]
lines = list(zip(lines[0], lines[1]))

ways, beats_record = [], 0
for race in lines:
    time, dist = race
    for i in range(1, time):
        if i * (time - i) > dist:
            beats_record += 1
    ways.append(beats_record)
    beats_record = 0

R = reduce(lambda x,y: x*y, ways)
print(R)
