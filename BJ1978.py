import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
C = 0

for i in range(N):
    B = 0
    for j in range(A[i]):
        if A[i] % (j + 1) == 0:
            B += 1

        else:
            continue

    if B == 2:
        C += 1

    else:
        continue

print(C)