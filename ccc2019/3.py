import sys
input = sys.stdin.readline
g = [input().split() for s in range(3)]
for i in range(3):
    for j in range(3):
        if g[i][j] != 'X':
            g[i][j] = int(g[i][j])

go = True
while go:
    for i in g:
        if i.count('X') == 1:
            pass#here
    for h in range(3):
        pass #here
    go = False