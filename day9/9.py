f = open("9.txt", "r")
msrmnts = [[int(x) for x in line.strip().split()] for line in f.readlines()]

def diffs(series):
    diff = []
    diff.append(series)

    def f(s):
        res = []
        for i, x in enumerate(s[1:]):
            res.append(x - s[i])
        return res

    diff.append(f(series))

    while any(x != 0 for x in diff[-1]):
        diff.append(f(diff[-1]))

    return diff[:-1]

p = []
for s in msrmnts:
    p.append(diffs(s))

R = 0
for l in p:
    r = 0
    for x in l:
        r += x[-1]
    R += r
print(R)
