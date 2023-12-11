# https://topaz.github.io/paste/#XQAAAQAcAgAAAAAAAAA0m0pnuFI8c+fPp4G3Y5M2miSs3R6AnrKm3fbDkugpdVsCgQOTZL/yzxGwy/N08UeBslxE7G36XluuSq4Y/2FE0+4nPcdj9lpkrrjBk5HRCFLEKuPjUV8tYPx04VDoJ1c6yyLzScmAGwNvzpPoqb5PkRyyy4dSEcuEDe/k0/U7h7pZVh4eTrNAIPsTNZohcltxuwuA4lrZSN37i0QZiufFpvLVyhV/dLBnmSr+2jwFcFE+W6OEIFQxK6MIJ2z7TWKj8lg6yV4yhJzTm+c+QHh2omzhGVLd2WdcHdhjmCyC+Btbr3yCqemYb/6tMUvz8VchnyHstx7QKKeLVmTOEyYqHH/qRDhlKXSQ23RWuPibCf4quQUPGpPDRsH4KITzLbIUVUdssnSp6ffcHO+dAISdzBOiznl5/+PI+jE=
import math as m, re, sys

board = list(open(sys.argv[1]))
symbols = {(r, c): [] for r in range(len(board)) for c in range(len(board))
         if board[r][c] not in '0123456789.' }

for r, row in enumerate(board):
    #print(f'row {r}: {row}')
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                for c in range(n.start() - 1, n.end() + 1)}
        #print('Edge', edge)
        for o in edge & symbols.keys():
            symbols[o].append(int(n.group()))

#print(symbols)
print(sum(sum(p) for p in symbols.values()))
print(sum(m.prod(p) for p in symbols.values() if len(p) == 2))
