import sys
input = sys.stdin.readline

import math

def prime(num):
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

for i in range(int(input())):
    n = int(input())
    avg = n * 2
    for j in range(3, n, 2):
        if prime(j) and prime(avg-j):
            print(j, avg-j)
            break





