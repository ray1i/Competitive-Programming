import sys
input = sys.stdin.readline

temp = input().split()
n = int(temp[0])
m = int(temp[1])
g = {}
temp = []
for i in range(1, n + 1):
    g[i] = []
for i in range(m):
    t = input().split()
    g[int(t[0])].append(int(t[1]))
    temp.append((int(t[0]), int(t[1])))

for i in temp:
    g[i[0]].remove(i[1])
    q = [1]
    v = [False for s in range(n + 1)]
    ans = 'NO'
    while q != []:
        for j in g[q[0]]:
            if j == n:
                ans = 'YES'
                q = [0]
                break
            elif v[j]:
                pass
            else:
                q.append(j)
                v[j] = True
        q.pop(0)
    print(ans)
    g[i[0]].append(i[1])
