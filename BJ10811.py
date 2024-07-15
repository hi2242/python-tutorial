import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = []
# B = 0

for x in range(0, N):
    A.append(x + 1)

# for x in range(0, M):
#     i, j = map(int, input().split())
#     for z in range(j - i, 0, -1):
#         for y in range(0, z):
#             B = A[i - 1 + y]
#             A[i - 1 + y] = A[i + y]
#             A[i + y] = B

for x in range(0, M):
    i, j = map(int, input().split())
    C = A[i - 1:j]
    C.reverse()
    A[i - 1:j] = C

for x in range(0, N):
    print(A[x], end = " ")
    