from pprint import pprint
file = open("day5data.txt").read().strip()

blocks = file.split("\n\n")

print(blocks)
seeds, *maps = blocks
seeds = [int(x) for x in seeds.split(':')[1].split()]

class MapsManip:
    def __init__(self, mapblock):
        lines = mapblock.split("\n")[1:] # řádky jednotlivých map bloků, bez nadpisu
        self.tuples = [[int(x) for x in line.split()] for line in lines]

    def traverse_interval(self, I):
        A = []
        for (dest, source, size) in self.tuples:
            source_end = source + size
            NR = []
            while I:
                (start, end) = I.pop()

                before = (start, min(end, source))
                intersect = (max(start, source), min(source_end, end))
                after = (max(source_end, start), end)
                if before[1] > before[0]:
                    NR.append(before)
                if intersect[1] > intersect[0]:
                    A.append( (intersect[0] - source + dest, intersect[1] - source + dest) )
                if after[1] > after[0]:
                    NR.append(after)
            I = NR
        return A+I

processed_maps = [MapsManip(mablock) for mablock in maps]
locations = []
pairs = list(zip(seeds[::2], seeds[1::2] ))
print(pairs)
for start, size in pairs:
    I = [(start, start + size)]
    for x in processed_maps:
        I = x.traverse_interval(I)
    locations.append(min(I)[0])
print(min(locations))



