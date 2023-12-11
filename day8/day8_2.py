import sys
from itertools import cycle
import re
import math

with open(sys.argv[1]) as file:
    [directions, raw_map] = file.read().strip().split('\n\n')
    print(f'Directions: {directions}\n')
    #print(f'raw_map: {raw_map}')

    map: dict[str, dict[str, str]] = {}
    for l in raw_map.split('\n'):
        root, l, r = re.findall(r'[A-Z1-9]{3}', l)
        map[root] = {"L": l, "R": r}

    #print(f'Map after parse:\n{map}\n')
    starts = [k for k in map.keys() if k[-1] == "A"]
    print(f'Starts: {starts}')

    def solve(a):
        k = a
        for steps, d in enumerate(cycle(directions)):
            if k[-1] == 'Z':
                print(f'{a}: exit found at {k} after {steps} steps')
                return steps
            k = map[k][d]

    solutions = [solve(s) for s in starts]
    print(f'\n{solutions}')
    print(f'All the paths sync up after {math.lcm(*solutions)} steps')

