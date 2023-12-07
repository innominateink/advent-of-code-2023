import sys

file = open(sys.argv[1])
lines = file.read()

blocks = [l.split(':')[1].strip().split('\n') for l in lines.split('\n\n')]
for b in blocks:
    for i, ns in enumerate(b):
        b[i] = [int(s) for s in ns.split(' ')]
[seeds, seedToSoil, soilToFert, fertToWater, waterToLight, lightToTemp, tempToHum, humToLoc] = blocks
seeds = seeds[0]

print('seeds:', seeds)
print('seeds to soil:', seedToSoil)

def isInRange(rangeStart, rangeLength, num):
    return num >= rangeStart and num < rangeStart + rangeLength 

def find(n, numlist):
    return next((Map for Map in numlist if isInRange(Map[1], Map[2], n)), [n, n, 1])

def getNextLocation(Maps, seed):
    Map = find(seed, Maps)
    return Map[0] + (seed - Map[1])

lowest_loc = 99999999999999

for si, seed in enumerate(seeds):
    print('\nseed:', seed)
    # seed -> soil
    soil = getNextLocation(seedToSoil, seed)
    print('destination soil:', soil)
    # soil -> fertilizer
    fert = getNextLocation(soilToFert, soil)
    print('destination fertilizer:', fert)
    # fertilizer -> water
    water = getNextLocation(fertToWater, fert)
    print('destination water:', water)
    # water -> light
    light = getNextLocation(waterToLight, water)
    print('destination light:', light)
    # light -> temp
    temp = getNextLocation(lightToTemp, light)
    print('destination temp:', temp)
    # temp -> humidity
    hum = getNextLocation(tempToHum, temp)
    print('destination humidity:', hum)
    # humidity -> location
    loc = getNextLocation(humToLoc, hum)
    print('destination location:', loc)
    if loc < lowest_loc:
        lowest_loc = loc

print('The lowest location found was', lowest_loc)
