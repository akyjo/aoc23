from math import sqrt
f = open("6.txt", "r")
lines = f.readlines()
lines = [ line.split(':')[1].strip() for line in lines]
lines = [int("".join(line.split())) for line in lines]
time, dist = lines
#
# i*i -i*lines[0] + lines[1] = 0
# ax*x + bx + c = 0
# D = b*b - 4ac
D = lines[0]**2 - 4*lines[1]
print(D)
i_1, i_2 = (-lines[0] + sqrt(D))/2, (-lines[0] - sqrt(D))/2
print(int(i_1), int(i_2))

range_start = -int(i_1)
while range_start * (time - range_start) < dist:
    range_start += 1

range_end = -int(i_2)
while range_end * (time - range_end) > dist:
    range_end += 1

print(range_end - range_start)
