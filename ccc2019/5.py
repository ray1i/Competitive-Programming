import sys
input = sys.stdin.readline

temp = input().split()
n = int(temp[0])
k = int(temp[1])

a = []
for i in range(n):
    a.append([int(s) for s in input().split()])

m = 0
for row in range(n - k + 1): #every row
    for col in range(row + 1):
        temp = 0
        for i in range(k):
            for j in range(i + 1):
                if a[i + row][j + col] > temp:
                    temp = a[i + row][j + col]
        m += temp
print(m)