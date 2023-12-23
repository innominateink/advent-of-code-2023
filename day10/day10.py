import sys
import re

file = open(sys.argv[1])
lines = list(file)
print(f'Map:\n{"".join(lines)}')

lines = [line.strip() for line in lines]


def findStart(strs):
    for idx, s in enumerate(strs):
        m = re.search('S', s)
        if m:
            return (idx, int(m.span()[0]))
    return None


# find the starting pipe
start = findStart(lines)
print(f'Start = {start}')


def findCon(r, c):
    char = lines[r][c]

    if r > 0:
        topchar = lines[r-1][c]
        top = ((r-1, c) if r >= 0
               and topchar in ['S', '7', '|', 'F']
               and char in ['S', 'J', '|', 'L']
               else None)
    else:
        top = None

    if c + 1 < len(lines[0]):
        rgtchar = lines[r][c+1]
        rgt = ((r, c+1) if rgtchar in ['S', 'J', '-', '7']
               and char in ['S', 'L', '-', 'F']
               else None)
    else:
        rgt = None

    if r + 1 < len(lines):
        botchar = lines[r+1][c]
        bot = ((r+1, c) if botchar in ['S', 'J', '|', 'L']
               and char in ['S', '7', '|', 'F']
               else None)
    else:
        bot = None

    if c > 0:
        lftchar = lines[r][c-1]
        lft = ((r, c-1) if lftchar in ['S', 'L', '-', 'F']
               and char in ['S', 'J', '-', '7']
               else None)
    else:
        lft = None

    return (top, rgt, bot, lft)


def findNextCon(t: tuple, prev: tuple):
    return [c for c in findCon(*t) if c is not None and c != prev]


print(' ', "".join([str(x) for x in list(range(0, len(lines[0])))]))

map = []
for idl, line in enumerate(lines):
    map.append(line)
    for anc, bdc in {
            'F': '╔', 'L': '╚', 'J': '╝', '7': '╗', '|': '║', '-': '═'
            }.items():
        map[idl] = map[idl].replace(anc, bdc)
    print(idl, map[idl])

# find the two sides of the starting pipe
# keep two pairs of coordinates, one for each side of the pipe
prev = (start, start)
current = findNextCon(start, (-1, -1))

i = 1
while not all(x == current[0] for x in current):
    temp = current
    print(f'Step {i} => Finding {current} from previous {prev}')
    current = [*findNextCon(current[0], prev[0]), *findNextCon(current[1], prev[1])]
    print(f'> {current} == {map[current[0][0]][current[0][1]]} {map[current[1][0]][current[1][1]]}')
    prev = temp
    print(f'> last: {prev}')
    i += 1
print(f'{i} steps')

# move the two pairs of coordinates to S's two sides
# add the distances as you go, stop when the coordinates cross
# how to know when distances cross?
