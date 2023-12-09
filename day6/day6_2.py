import sys

def solve(x, t):
    return x * (t - x)

with open(sys.argv[1]) as file:
    [time, distance] = [int("".join(l.split()[1:])) for l in file.readlines()]
    print(f'time:     {time}ms')
    print(f'distance: {distance}mm')
    print(f'x * ({time} - x) > {distance}')
    solutions = [solve(x, time) for x in range(1, time) if solve(x,time) > distance]
    print(f'This race can be won in {len(solutions)} different ways')

