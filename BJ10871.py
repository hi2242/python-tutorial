import sys

input = sys.stdin.readline

N, X = map(int, input().split())

A = list(map(int, input().split()))

for i in range(0, N):
    if A[i] < X:
        print(A[i], end = " ")

    else:
        continue
# B = []
# j = int(0)
# for i in range(0, N):
#     if A[i] < X:
#         B.append(A[i])
#         j = j + 1

# for i in range(0, j):
#     print(B[i], end = " ")