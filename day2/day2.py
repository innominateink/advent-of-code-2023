import fileinput
import re

sum = 0
for line in fileinput.input():
    [tag,games] = line.split(': ')
    id = tag.split( )[1]
    rs = [int(x) for x in re.findall(r'(\d+) red', games)]
    gs = [int(x) for x in re.findall(r'(\d+) green', games)]
    bs = [int(x) for x in re.findall(r'(\d+) blue', games)]
    power = max(rs) * max(gs) * max(bs)
    sum = sum + power
    print(id, games, rs, max(rs), gs, max(gs), bs, max(bs), power, sum)
    pass
print ('the sum is ', sum)
