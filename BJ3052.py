import sys

input = sys.stdin.readline
B = []
C = 0

for i in range(0, 10):
    A = int(input())
    B.append(A % 42)

for i in range(0, 42):
    if B.count(i) >= 1:
        C = C + 1

    else:
        continue

print(C)