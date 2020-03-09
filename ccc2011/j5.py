l = int(input())
o = {}
v = {}
for i in range(1, l + 1):
    o[i] = []
    v[i] = 1
for i in range(1, l):
    o[int(input())].append(i)

for i in range(1, l + 1):
    if o[i] == []:
        v[i] = 2
    else:
        for j in o[i]:
            v[i] *= v[j]
        v[i] += 1

print(v[l] - 1)