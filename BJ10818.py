import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

print(min(A), max(A))

# import sys

# input = sys.stdin.readline

# N = int(input())

# A = list(map(int, input().split()))
# B = 0

# for i in range(0, N - 1):
#     for j in range(i + 1, N):
#         if A[i] > A[j]:
#             B = A[i]
#             A[i] = A[j]
#             A[j] = B

#         else:
#             continue

# print(A[0], A[4])