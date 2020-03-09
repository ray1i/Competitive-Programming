a = [False for s in range(int(input()) + 1)]

c = 0
go = True
for i in range(int(input())):
    if go:
        g = int(input())
        for j in range(g, -1, -1):
            if j == 0:
                go = False
                break
            if not a[j]:
                a[j] = True
                c += 1
                break
    else:
        break

print(c)

