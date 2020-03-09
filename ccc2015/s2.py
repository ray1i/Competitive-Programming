import sys
input = sys.stdin.readline

j = int(input())
a = int(input())
sizes = {'S':0, 'M':1, 'L':2}

jer = []
for i in range(j):
    jer.append(sizes[input().strip()])

c = 0
for i in range(a):
    temp = input().split()
    temp[0] = sizes[temp[0]]
    temp[1] = int(temp[1]) - 1
    if temp[1] < len(jer):
        if jer[temp[1]] >= temp[0]:
            c += 1
            jer[temp[1]] = -1
print(c)