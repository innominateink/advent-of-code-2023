import sys
import math

file = open(sys.argv[1])
lines = file.readlines()

# keep track of score total
score = 0
# keep track of how many cards have been processed
cards = 0
# keep a stack of how many copies we've earned for the next cards
stack = []

for i, line in enumerate(lines):
    # count the number of copies (original + copies earned from previous cards)
    copies = stack.pop(0) + 1 if len(stack) > 0 else 1
    # increment total number of cards
    cards = cards + copies

    # Get lists of the winning and card numbers
    [winNums, yourNums] = [l.strip().split(' ') for l in line.split(':')[1].split('|')]

    # Filter for the card numbers that are also winning numbers and count how many
    matches = len([n for n in winNums if len(n) > 0 and yourNums.count(n) > 0])

    # create stack positions if they don't exist yet
    if len(stack) < matches:
        stack.extend([0 for i in range(matches - len(stack))])
    # add nr of copies to each of the next matches positions in stack
    for s in range(matches):
        stack[s] = stack[s] + copies

    # You get 2^n points, where n = number of winning numbers
    if matches > 0:
        score = score + math.floor(pow(2, matches - 1))

print("The score total is ", score)
print("Total number of cards is ", cards)
