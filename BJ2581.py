import sys

input = sys.stdin.readline

M = int(input())
N = int(input())

A = []

while M <= N:
    for i in range(M - 1):
        if i != 0 and M % (i + 1) == 0:
            break

        elif M == i + 2:
            A.append(M)

        else:
            continue
    M += 1

if len(A) != 0:
    print(sum(A))
    print(A[0])

else:
    print(-1)