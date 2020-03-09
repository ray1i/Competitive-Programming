temp = input().split()
n = int(temp[0])
m = int(temp[1])
g = [input() for s in range(n)]

act = [['_' for s in range(m)] for t in range(n)]
step = [[-2 for s in range(m)] for t in range(n)]
for i in range(n):
    for j in range(m):
        if act[i][j] == '_':
            act[i][j]=g[i][j]
        if g[i][j] == 'S':
            start = (i, j)
            step[i][j] = 0
        elif g[i][j] == 'C':
            u = i - 1 #up
            while True:
                if g[u][j] == '.':
                    act[u][j] = 'W'
                    step[u][j] = -1
                elif g[u][j] == 'W':
                    break
                u -= 1
            u = i + 1 #down
            while True:
                if g[u][j] == '.':
                    act[u][j] = 'W'
                    step[u][j] = -1
                elif g[u][j] == 'W':
                    break
                u += 1
            u = j - 1 #left
            while True:
                if g[i][u] == '.':
                    act[i][u] = 'W'
                    step[i][u] = -1
                elif g[i][u] == 'W':
                    break
                u -= 1
            u = j + 1 #right
            while True:
                if g[i][u] == '.':
                    act[i][u] = 'W'
                    step[i][u] = -1
                elif g[i][u] == 'W':
                    break
                u += 1
        elif g[i][j] == '.' and act[i][j] != 'W':
            step[i][j] = 0

udlr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def con(x, y, hor, ver):
    global act, step, q, visited
    #print(act)
    #print(y + ver, x + hor)
    #print(act[y + hor][x + ver])
    if act[y + ver][x + hor] == 'U':
        v = -1
        h = 0
        #print('yes')
    elif act[y + ver][x + hor] == 'D':
        v = 1
        h = 0
        #print('yes')
    elif act[y + ver][x + hor] == 'L':
        v = 0
        h = -1
    elif act[y + ver][x + hor] == 'R':
        v = 0
        h = 1
    #print(v, h)
    while act[y + v + ver][x + h + hor] != 'W':
        #print(act[y + ver][x + hor], y + v + ver, x + h + hor)
        if act[y + v + ver][x + h + hor] == '.':
            q.append((y + v + ver, x + h + hor))
            step[y + v + ver][x + h + hor] = step[y][x] + 1
            break
        visited[y + v + ver][x + h + hor] = True
        if v < 0:
            v -= 1
        elif v > 0:
            v += 1
        elif h < 0:
            h -= 1
        elif h > 0:
            h += 1
        

def check(x, y):
    global act, step, q, udlr, visited
    for i in udlr:
        #print(i[0],i[1], y, x)
        if not visited[y + i[0]][x + i[1]]:
            #print(act[y + i[0]][x + i[1]])
            if act[y + i[0]][x + i[1]] == '.':
                q.append((y + i[0], x + i[1]))
                step[y + i[0]][x + i[1]] = step[y][x] + 1
            elif act[y + i[0]][x + i[1]] in ['U', 'D', 'L', 'R']:
                visited[y + i[0]][x + i[1]] = True
                con(x, y, i[1], i[0])
                

#print(step)
#print(act)
q = [start]
visited = [[False for s in range(m)] for t in range(n)]
while q != []:
    #print(q)
    #print(visited)
    y = q[0][0]
    x = q[0][1]
    check(x, y)
    visited[y][x] = True
    q.pop(0)
    #print(visited)

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if step[i][j] != -2 and (i, j) != start:
            if step[i][j] == 0:
                print(-1)
            else:
                print(step[i][j])

