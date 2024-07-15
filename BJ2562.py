import sys

input = sys.stdin.readline
B = []

for i in range(0, 9):
    A = int(input())
    B.append(A)

print(max(B))
print(B.index(max(B)) + 1)