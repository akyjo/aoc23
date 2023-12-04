from collections import defaultdict
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

win_cards = []

for j, card in enumerate(scratchcards, 1):
    i = 0
    for number in card[0]:
        if number in card[1]:
            i += 1
    win_cards.append([str("card_") + str(j), i]) #ordinal num of card and how many cards it wins

card_counter = defaultdict(lambda: 1) # init counter to 1
for c in win_cards:
    card_counter[c[0]]

for i, card in enumerate(win_cards, 1):
    for j in range(i + 1 ,i + 1 + card[1]):
        card_counter["card_" + str(j)] += card_counter[card[0]]

print(sum(_ for _ in card_counter.values()))
