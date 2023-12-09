import sys
import math
from collections import Counter

def get_card_strength(c):
    if c == 'A':
        return 14
    elif c == 'K':
        return 13
    elif c == 'Q':
        return 12
    elif c == 'J':
        return 11
    elif c == 'T':
        return 10
    elif c == 'J':
        return 1
    else:
        return int(c)

# 0 = high card, 1 = one pair, 2 = two pair, 3 = three of a kind, 4 = full house, 5 = four of a kind, 6 = five of a kind
def get_hand_strength(s):
    cards = Counter(s).most_common()
    # strength = "".join([get_card_strength(c) for c in s])

    # ss = reversed([get_card_strength(c) for c in s])
    # strength = sum([st * math.pow(10, i * 2) for i, st in enumerate(ss)])

    # ss = reversed([get_card_strength(c) for c in s])
    strength = sum([get_card_strength(c) * math.pow(10, i * 2) for i, c in enumerate(reversed(s))])
    print(strength)

    # len 5: high card
    if len(cards) == 5:
        return strength
    # len 4: one pair
    elif len(cards) == 4:
        return strength + (1 * math.pow(10, 10))
    # len 3: two pair, three of a kind
    elif len(cards) == 3:
        if cards[0][1] == 2:
            return strength + (2 * math.pow(10, 10))
        elif cards[0][1] == 3:
            return strength + (3 * math.pow(10, 10))
    # len 2: full house, four of a kind
    elif len(cards) == 2:
        if cards[0][1] == 4:
            return strength + (5 * math.pow(10, 10))
        elif cards[0][1] == 3:
            return strength + (4 * math.pow(10, 10))
    # len 1: five of a kind
    elif len(cards) == 1:
        return strength + (6 * math.pow(10, 10))

with open(sys.argv[1]) as file:
    lines = file.read().splitlines()
    hands = [tuple(l.split(' ')) for l in lines]
    hands.sort(key=lambda a: get_hand_strength(a[0]))
    score = sum([int(h[1]) * (i + 1) for i, h in enumerate(hands)])
    print(score)
