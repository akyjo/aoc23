from pprint import pprint
f = open("day5data.txt", "r")
lines = f.readlines()
#
# [ 50, 98, 2 ]
# destination, source, range for both - including; i.e.: 50, 98, 2 ->
# -> 50,51 destination 98,99 source
#
maps = {}
seeds = lines[0]
seeds = [int(seed) for seed in seeds.split(":")[1][1:].split(" ")]

for line in lines[1:]: #skip first line
    if "map" in line:
        lastkey = line.split(" ")[0]
        maps[lastkey] = []
    elif len(line) < 2:
        continue
    else:
        maps[lastkey].append(list(map(int, line.split(" "))))

# pprint(maps)
# for map in maps:
#     print(map, "->", maps[map])
flag, k = False, 0

locations = []
for seed in seeds:
    k = seed
    for key in maps:

        for row in maps[key]:

            if k >= row[1] and k <= (row[1] + row[2]):
                k = (row[0] + (k - row[1]))
                flag = True
                break

            if flag:
                break

        flag = False
    locations.append(k)
print(min(locations))
