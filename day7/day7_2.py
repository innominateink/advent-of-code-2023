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
    elif c == 'T':
        return 10
    elif c == 'J':
        return 1
    else:
        return int(c)

# 0 = high card, 1 = one pair, 2 = two pair, 3 = three of a kind, 4 = full house, 5 = four of a kind, 6 = five of a kind
def get_hand_strength(s):
    print('')
    print('card:', s)
    c = Counter(s)
    print('counts:', c)

    most_common = c.most_common(1)[0]

    if most_common[0] == 'J' and len(c) > 1:
        most_common = c.most_common(2)[1]

    jokers = c['J']
    del c['J']

    print(f'most_common={most_common} jokers={jokers}')

    c.update(**{most_common[0]: jokers})

    print('counts after jokers:', c)
    cards = c.most_common()
    print('how many types of cards?', len(cards))

    list_strength = [get_card_strength(c) * math.pow(10, i * 2) for i, c in enumerate(reversed(s))]
    strength = sum(list_strength)
    print('strength:', strength, list_strength)

    # len 5: high card
    if len(cards) == 5:
        print('high card')
        return strength
    # len 4: one pair
    elif len(cards) == 4:
        print('one pair')
        return strength + (1 * math.pow(10, 10))
    # len 3: two pair, three of a kind
    elif len(cards) == 3:
        if cards[0][1] == 2:
            print('two pair')
            return strength + (2 * math.pow(10, 10))
        elif cards[0][1] == 3:
            print('three of a kind')
            return strength + (3 * math.pow(10, 10))
    # len 2: full house, four of a kind
    elif len(cards) == 2:
        if cards[0][1] == 4:
            print('four of a kind')
            return strength + (5 * math.pow(10, 10))
        elif cards[0][1] == 3:
            print('full house')
            return strength + (4 * math.pow(10, 10))
    # len 1: five of a kind
    elif len(cards) == 1:
        print('five of a kind')
        return strength + (6 * math.pow(10, 10))

with open(sys.argv[1]) as file:
    lines = file.read().splitlines()
    hands = [tuple(l.split(' ')) for l in lines]
    hands.sort(key=lambda a: get_hand_strength(a[0]))
    print('hands:', hands)
    score = sum([int(h[1]) * (i + 1) for i, h in enumerate(hands)])
    print('score:', score)
