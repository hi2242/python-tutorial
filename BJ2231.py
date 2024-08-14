import sys

input = sys.stdin.readline

N = int(input())

for i in range(9 * len(str(N)), len(str(N)) - 1, -1):
    A = N - i
    B = 0
    if A > 0:
        for j in range(0, len(str(A))):
            B += int(str(A)[j])

    if B == i:
        print(A)
        break

    elif i == len(str(N)):
        print(0)

    else:
        continue