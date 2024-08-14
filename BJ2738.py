import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = []
B = []

for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    B.append(list(map(int, input().split())))

C = [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]

# for row in C:
#     print(*row, end="\n")

for row in C:
    print(' '.join(map(str, row)))