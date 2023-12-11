import sys

# histories
hs = [[int(n) for n in l.strip().split(' ')] for l in list(open(sys.argv[1]))]

def find_next(h):
    print(f'History: {h}')
    # calculate all the differences all the way down
    layers = [h]
    last = layers[0]
    # while not all numbers are the same
    while not all(x == last[0] for x in last):
        # calculate all the differences by zipping each number with the next one
        last = [j-i for i, j in zip(last[:-1], last[1:])]
        layers.append(last)
        print(f'Differences: {last}')

    # now go back up through the layers and append to each layer
    # starting from -1, the last position of the previous layer
    # + the last position of the current layer
    print(last)
    for idx, layer in enumerate(reversed(layers[:-1])):
        #layer.append(layer[-1] + layers[idx - 1][-1])
        print(f'{idx} {layer} {layer[-1]} {last[-1]}')
        layer.append(layer[-1] + last[-1])
        layer.insert(0, layer[0] - last[0])
        last = layer
        print(f'layer changed to {layer}')
    print(last)
    print('')
    return (last[0], last[-1])

result = [find_next(h) for h in hs]
[sum_of_prev, sum_of_next] = [sum(x) for x in list(zip(*result))]
print('The sum of all next numbers is ', sum_of_next)
print('The sum of all previous numbers is ', sum_of_prev)
