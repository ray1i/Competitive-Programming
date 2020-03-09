import sys
input = sys.stdin.readline

list = []
for i in range(int(input())):
    a = int(input())
    if a == 0:
        del list[-1]
    else:
        list.append(a)

print(sum(list))