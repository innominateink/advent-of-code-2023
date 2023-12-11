# seed, soil, fert, water, light, temp, hum, loc
import sys
import math

# dest src range
#def get_range(s):
#    return ((s[1], s[1] + s[2] - 1),(s[0], s[0] + s[2] - 1))

file = open(sys.argv[1])
lines = file.read()

maps = [l.split(':')[1].strip().split('\n') for l in lines.split('\n\n')]
for m in maps:
    for i, ns in enumerate(m):
        m[i] = [int(s) for s in ns.split(' ')]

seeds = maps[0][0]
seeds = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]

# maps = [[get_range(l) for l in m] for m in maps[1:]]

# now they're (src, dest, len) and sorted
maps = [[(l[1], l[0], l[2]) for l in sorted(m, key=lambda a: a[1])] for m in maps[1:]]

print('seeds:', seeds)
print('maps:', maps)
print('')

lowest = 99999999999
for src, dest in seeds:
    print(f'seed full range: {src} -> {dest}\n')

    # this should keep the current ranges being worked on, we want to transform each of these into
    # all the ranges for the next layer
    ranges = [(src, dest)]

    temp = ranges[0]
    print('temp:', temp)

    # go through each layer, converting all ranges from one to the next
    for m in maps:
        print('current map:', m)
        # need to know if they're sufficiently contained in the destination ranges,
        # so need to break up ranges into something that fits the current map
        # for each of these ranges, if they're not contained, break them up
        for src, dest in ranges:
            # find the map range that satisfies this src
            print('found range:', next((ran for ran in m if ran[0] <= src)))
            print(src, dest)
        print('ranges:', ranges)

    print('')
print('lowest:', lowest)
