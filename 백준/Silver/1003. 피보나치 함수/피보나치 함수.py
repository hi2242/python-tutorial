import sys
from collections import deque

def solve(n):
    d = deque([0, 1])

    if N == 0:
        print(1, 0)

    elif N == 1:
        print(0, 1)

    else:
        for _ in range(N - 1):
            d.append(d.popleft() + d[0])
        print(d[0], d[1])

input = sys.stdin.readline

T = int(input())

A = []


for _ in range(T):
    N = int(input())
    solve(N)