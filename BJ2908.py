import sys

input = sys.stdin.readline
C = []
D = []
A, B = map(str, input().split())

for i in range(0, 3):
    C.append(A[2 - i])
    D.append(B[2 - i])

for i in range(0, 3):
    if C[i] > D[i]:
        for j in range(0, 3):
            print(C[j], end = "")
        break

    elif D[i] > C[i]:
        for j in range(0, 3):
            print(D[j], end = "")
        break

    else:
        continue