g = [1, 2, 3, 4]
h = [1, 2, 3, 4]

seq = input()

for i in range(len(seq)):
    if seq[i] == 'H':
        h[0] = g[2]
        h[1] = g[3]
        h[2] = g[0]
        h[3] = g[1]
        g = h.copy()
        
    elif seq[i] == 'V':
        h[0] = g[1]
        h[1] = g[0]
        h[2] = g[3]
        h[3] = g[2]
        g = h.copy()

print(g[0], g[1])
print(g[2], g[3])