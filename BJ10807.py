import sys

input = sys.stdin.readline

N = int(input())
# T = int(0)

A = list(map(int, input().split()))

v = int(input())

# for i in range(0, N):
#     if A[i] == v:
#         T = T + 1

print(A.count(v))