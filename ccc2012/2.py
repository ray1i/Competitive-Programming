ro = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
i = input()
t = 0
for n in range(0, len(i), 2):
    if n + 3 < len(i):
        if ro[i[n + 1]] >= ro[i[n + 3]]:
            t += int(i[n]) * ro[i[n + 1]]
        else:
            t -= int(i[n]) * ro[i[n + 1]]
    else:
        t += int(i[n]) * ro[i[n + 1]]
print(t)