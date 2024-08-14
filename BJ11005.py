import sys

input = sys.stdin.readline

N, B = map(int, input().split())
F = 0
A = []

for i in range(30, -1, -1):
    if int(N / (B ** i)) != 0:
        F = i
        break
    else:
        continue

for i in range(F, -1, -1):
    A.append(int(N / (B ** i)))
    N -= int(N / (B ** i)) * (B ** i)

for i in range(len(A)):
    if 10 <= A[i] <= 36:
        A[i] = chr(A[i] + 55)

    else:
        continue

print(*A, sep="")