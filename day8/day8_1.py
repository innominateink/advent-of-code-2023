# 16579
import sys
from itertools import cycle
import re

with open(sys.argv[1]) as file:
    [directions, raw_map] = file.read().strip().split('\n\n')
    print(f'Directions: {directions}')

    map: dict[str, dict[str, str]] = {}
    for l in raw_map.split('\n'):
        root, l, r = re.findall(r'[A-Z]{3}', l)
        map[root] = {"L": l, "R": r}

    print(f'Map after parse:\n{map}\n')

    k = 'AAA'
    for steps, d in enumerate(cycle(directions)):
        #print(f'Step {steps + 1}: {k} {node} => {d} => {node[d]} {map[node[d]]}')
        if k == 'ZZZ':
            print(f'Steps: {steps}')
            break
        k = map[k][d]

