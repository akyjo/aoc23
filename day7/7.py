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

card_strength_map = {"2" : 0,
                 "3" : 1,
                 "4" : 2,
                 "5" : 3,
                 "6" : 4,
                 "7" : 5,
                 "8" : 6,
                 "9" : 7,
                 "T" : 8,
                 "J" : 9,
                 "Q" : 10,
                 "K" : 11,
                 "A" : 12,
                 }

def get_hand_type(hand):

    _cter = Counter()
    for _ in hand:
        _cter[_] += 1
    _cards_repeated = sorted(list(_cter.values()), reverse=True)

    # five_o_k 5       - len 1
    # four_o_k 4, 1    - len 2
    # full_house 3, 2  - len 2
    # three_o_k 3, 1, 1- len 3
    # two_pair 2, 2, 1 - len 3
    # pair 2, 1, 1, 1  - len 4
    # hi 1, 1, 1, 1, 1 - len 5

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
    hand_type_ord = get_hand_type(handstr).value
    return (hand_type_ord, *card_strength(handstr))

sorted_hands = sorted(hands, key=sort_key)
res = 0

for i, hand in enumerate(sorted_hands, 1):
    res += i * hand[1]
print(res)
