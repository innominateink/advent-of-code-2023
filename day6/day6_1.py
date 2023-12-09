import sys

def solve(x, t):
    return x * (t - x)

answer = 1;
with open(sys.argv[1]) as file:
    [times, distances] = [[int(n) for n in l.split()[1:]] for l in file.readlines()]
    print('times:    ', times)
    print('distances:', distances)
    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        print('for', time, 'ms and', distance, 'mm')
        print('x.(', time, '- x) > ', distance)
        solutions = [solve(x, time) for x in range(1, time) if solve(x,time) > distance]
        answer = answer * len(solutions)
print(answer)
