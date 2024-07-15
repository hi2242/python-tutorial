import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = []
B = 0

for x in range(0, N):
    A.append(x + 1)

for x in range(0, M):
    i, j = map(int, input().split())
    B = A[i - 1]
    A[i - 1] = A[j - 1]
    A[j - 1] = B

for x in range(0, N):
    print(A[x], end = " ")