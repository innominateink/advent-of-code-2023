import sys
import math

file = open(sys.argv[1])
lines = file.read()

blocks = [l.split(':')[1].strip().split('\n') for l in lines.split('\n\n')]
for b in blocks:
    for i, ns in enumerate(b):
        b[i] = [int(s) for s in ns.split(' ')]
[seeds, seedToSoil, soilToFert, fertToWater, waterToLight, lightToTemp, tempToHum, humToLoc] = blocks
seeds = seeds[0]
seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

def isInRange(rangeStart, rangeLength, num):
    return num >= rangeStart and num < rangeStart + rangeLength 

def find(n, numlist):
    return next((Map for Map in numlist if isInRange(Map[1], Map[2], n)), [n, n, 1])

def getNextLocation(Maps, seed):
    Map = find(seed, Maps)
    return Map[0] + (seed - Map[1])

lowest_loc = 99999999999999

print('seeds:', seeds)
for src, ran in seeds:
    print('src', src, 'ran', ran)
    for seed in range(src, src + ran):
        # seed -> soil
        soil = getNextLocation(seedToSoil, seed)
        # soil -> fertilizer
        fert = getNextLocation(soilToFert, soil)
        # fertilizer -> water
        water = getNextLocation(fertToWater, fert)
        # water -> light
        light = getNextLocation(waterToLight, water)
        # light -> temp
        temp = getNextLocation(lightToTemp, light)
        # temp -> humidity
        hum = getNextLocation(tempToHum, temp)
        # humidity -> location
        loc = getNextLocation(humToLoc, hum)
        if loc < lowest_loc:
            print('\nseed:', seed)
            print('lowest location was', lowest_loc, 'now is', loc)
            lowest_loc = loc

print('The lowest location found was', lowest_loc)
