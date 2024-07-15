import sys

input = sys.stdin.readline
A = []
B = []

for i in range(0, 28):
    n = int(input())
    A.append(n)

for i in range(0, 30):
    B.append(i + 1)

for i in range(0, 28):
    B.remove(A[i])

print(min(B), max(B))