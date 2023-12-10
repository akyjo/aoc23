from collections import Counter
from enum import Enum, auto

f = open("day7data.txt", "r")
hands = f.readlines()
hands = [ line.strip().split(" ") for line in hands]
hands = [(line[0], int(line[1])) for line in hands]

class HandType(Enum):
    hi = auto()
    pair = auto()
    two_pair = auto()
    triple = auto()
    full_house = auto()
    quad = auto()
    quint = auto()

card_strength_map = {
                 "J" : 0,
                 "2" : 1,
                 "3" : 2,
                 "4" : 3,
                 "5" : 4,
                 "6" : 5,
                 "7" : 6,
                 "8" : 7,
                 "9" : 8,
                 "T" : 9,
                 "Q" : 10,
                 "K" : 11,
                 "A" : 12,
                 }

def get_hand_type(hand):

    _cter = Counter()
    for _ in hand:
        _cter[_] += 1
    _cards_repeated = sorted(list(_cter.values()), reverse=True)

    match len(_cards_repeated):
        case 1: 
            return HandType.quint
        case 2: 
            if _cards_repeated[0] == 4:
                return HandType.quad
            else:
                return HandType.full_house
        case 3: 
            if _cards_repeated[0] == 3:
                return HandType.triple
            else:
                return HandType.two_pair
        case 4: 
            return HandType.pair
        case 5: 
            return HandType.hi

def get_jokerhand_type(hand):
    #five js edge case
    if hand == "JJJJJ":
        return HandType.quint

    hand_wo_joker = hand.replace("J", "")
    _cter = Counter()

    for _ in hand_wo_joker:
        _cter[_] += 1

    _cards_repeated = sorted(list(_cter.values()), reverse=True)

    js = 5 - len(hand_wo_joker)
    print(_cards_repeated, " ", end="")
    _cards_repeated[0] += js

    print(hand,hand.replace("J", ""), _cards_repeated)

    match len(_cards_repeated):
        case 1: 
            return HandType.quint
        case 2: 
            if _cards_repeated[0] == 4:
                return HandType.quad
            else:
                return HandType.full_house
        case 3: 
            if _cards_repeated[0] == 3:
                return HandType.triple
            else:
                return HandType.two_pair
        case 4: 
            return HandType.pair
        case 5: 
            return HandType.hi

def card_strength(card):
    return tuple(card_strength_map[c] for c in card)

def sort_key(hand):
    handstr, _ = hand
    hand_type_ord = get_jokerhand_type(handstr).value if "J" in handstr else get_hand_type(handstr).value
    return (hand_type_ord, *card_strength(handstr))

sorted_hands = sorted(hands, key=sort_key)
res = 0

for i, hand in enumerate(sorted_hands, 1):
    res += i * hand[1]
print(res)
