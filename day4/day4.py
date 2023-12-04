f = open("day4data.txt", "r")
lines = [line.split(":")[1][1:-1] for line in f.readlines()] #lines processing
lines = [line.split("|") for line in lines]
scratchcards, card, points = [], [], []

for line in lines:
    for record in line:
        record = list(map(int, filter(lambda x: len(x) > 0,record.split(" "))))
        card.append(record)
    scratchcards.append(card)
    card =[]

for card in scratchcards:
    i = 0
    for number in card[0]:
        if number in card[1]:
            i += 1
    points.append(pow(2, i-1) if i > 0 else 0) # need to subtract 1 to score 0 correctly

print(sum(points))
