r = [0 for s in range(1001)]
for i in range(int(input())):
    r[int(input())] += 1
f = [1]
s = [1]
for i in range(len(r)):
    if r[i] != 0:
        if r[i] > f[0]:
            s = f.copy()
            f = [r[i], i]
        elif r[i] == f[0]:
            f.append(i)
        elif r[i] == s[0]:
            s.append(i)
g = 0
if len(f) > 2:
    s = f
for i in range(1, len(f)):
    for j in range(1, len(s)):
        if abs(f[i] - s[j]) > g:
            g = abs(f[i] - s[j])
print(g)