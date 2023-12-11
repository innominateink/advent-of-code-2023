import sys
import re
from enum import Enum

numbers = Enum('numbers', ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])

lines = list(open(sys.argv[1]))
totalp1 = 0
totalp2 = 0
for line in lines:
    print(line.strip())
    # part 1
    first = next((c for c in line if c.isnumeric()), 0)
    last = next((c for c in reversed(line) if c.isnumeric()), 0)
    print(first, last, '\n')
    totalp1 += int(first + last)

    # part 2
    ns = [d if d.isnumeric() else str(numbers[d].value - 1) for d in re.findall(r'(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))', line)]
    print(ns, '\n')
    totalp2 += int(ns[0] + ns[-1])
    

print('Part 1 total =', totalp1)
print('Part 2 total =', totalp2)
