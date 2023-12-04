import sys
import math

file = open(sys.argv[1])
lines = file.readlines()

total = 0

for i, line in enumerate(lines):
    # Get lists of the winning and card numbers
    [winNums, yourNums] = [l.strip().split(' ') for l in line.split(':')[1].split('|')]
    # Filter for the card numbers that are also winning numbers
    matches = [n for n in winNums if len(n) > 0 and yourNums.count(n) > 0]
    # You get 2^n points, where n = number of winning numbers
    if len(matches) > 0:
        total = total + math.floor(pow(2, len(matches) - 1))
print("The point total is ", total)
