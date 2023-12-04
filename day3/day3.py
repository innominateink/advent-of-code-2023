import sys
import re

symbol = '[^.0-9\n]'
file = open(sys.argv[1])
lines = file.readlines()

def findCharsAround(row, start, end):
    chars = []
    # search top and bottom lines for symbols
    for i in range(max(0, start), end + 1):
        # search top line
        if re.match(symbol, lines[row - 1][i]):
            chars.append(lines[row - 1][i])
        # search bottom line
        if row + 1 < len(lines) and re.match(symbol, lines[row + 1][i]):
            chars.append(lines[row + 1][i])

    # search left and right of number for symbols
    if start > 0 and re.match(symbol, line[start]):
        chars.append(line[start])
    if end < len(line) and re.match(symbol, line[end]):
        chars.append(line[end])
    return chars

partNumberSum = 0

def isGear(row, col):
    char = lines[row][col]
    if (char == '*'):
        print(row, col)

# go through each line
for rowId, line in enumerate(lines):
    numbers = re.finditer('(\d+)', line)
    print(line)

    # for each of the numbers
    for match in numbers:
        [start, end] = match.span()
        chars = findCharsAround(rowId, start - 1, end)

        # if we picked up any symbols, it's a part number
        if len(chars) > 0:
            partNumberSum = partNumberSum + int(match.group()) # match.group returns the matched string

    gears = re.finditer(r'\*', line)
    for match in gears:
        [pos, end] = match.span()
        print(pos, end)
        nums = []
        # left
        if pos > 0 and line[pos - 1].isnumeric():
            nums.append(int(line[pos - 1]))
        # right
        if pos < len(line) and line[pos + 1].isnumeric():
            nums.append(int(line[pos + 1]))
        if rowId > 0:
            topline = lines[rowId - 1][pos - 1:end + 1]
            nums = nums + topline.strip('.').split('.')
        if rowId < len(lines):
            botline = lines[rowId + 1][pos - 1:end + 1]
            nums = nums + botline.strip('.').split('.')

        if len(nums) == 2:
            gearratio = int(nums[0]) * int(nums[1])
            print(pos, nums, gearratio)

print('Part 1:', partNumberSum)
