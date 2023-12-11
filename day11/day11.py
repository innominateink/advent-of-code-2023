import sys


# the distance between two pairs of coordinates is the sum of the distance
# between each member of the pair
def distance_between(a: tuple, b: tuple):
    return sum((abs(a[0] - b[0]), abs(a[1] - b[1])))

file = open(sys.argv[1]).read().strip()

# universe
u = file.splitlines()
xlen = len(u[0])
ylen = len(u)
print(f'This is a {xlen}x{ylen} universe')
print(f'The universe before expansion:\n{file}')

# cosmic expansion
empty_rows = [idr for idr, r in enumerate(u) if all(c == '.' for c in r)]
print(f'The empty rows are {empty_rows}')
empty_cols = [c for c in range(xlen) if all(r[c] == '.' for r in u)]
print(f'The empty columns are {empty_cols}')

# galaxies
gs = [(r, c) for r in range(len(u)) for c in range(len(u[0])) if u[r][c] == '#']
gsl = len(gs)
print(f'There are {gsl} galaxies:\n{gs}')

# distances between unique pairs of galaxies
distancespt1 = []
distancespt2 = []
for idg, g, in enumerate(gs):
    for idh in range(idg+1, gsl):
        xs, ys = [sorted((a,b)) for a,b in list(zip(g, gs[idh]))]
        rows_between = len([r for r in empty_rows if xs[0] < r < xs[1]])
        cols_between = len([r for r in empty_cols if ys[0] < r < ys[1]])
        # add one extra row per row between
        distancespt1.append(distance_between(g, gs[idh]) + rows_between + cols_between)
        # add one million rows per row between
        factor = 1000000
        distancespt2.append(distance_between(g, gs[idh]) + (rows_between * (factor - 1)) + (cols_between * (factor - 1)))

print(f'The part 1 solution is {sum(distancespt1)}')
print(f'The part 2 solution is {sum(distancespt2)}')
