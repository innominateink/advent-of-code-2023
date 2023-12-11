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
print(f'There are {len(gs)} galaxies:\n{gs}')
gsl = len(gs)

# distances between unique pairs of galaxies
distances = []
for idg, g, in enumerate(gs):
    for idh in range(idg+1, gsl):
        print(f'Pair {g} {gs[idh]}')
        rows_between = [c for c in empty_rows if g[0] < c < gs[idh][0]]
        print('Rows between:', rows_between)
        cols_between = [r for r in empty_cols if g[1] < r < gs[idh][1]]
        print('Columns between:', cols_between)
        distances.append(distance_between(g, gs[idh]) + (len(rows_between) + len(cols_between)))

print(f'The sum of all distances between pairs of galaxies is {sum(distances)}')
