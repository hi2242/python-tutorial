import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = []

for x in range(0, N):
    A.append(0)

for x in range(0, M):
    i, j, k = map(int, input().split())

    for y in range(i - 1, j):
        A[y] = k

for x in range(0, N):
    print(A[x], end = " ")