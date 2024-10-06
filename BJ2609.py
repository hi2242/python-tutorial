import sys

def solveYak(A, B):
    yak = 0
    if A > B:
        for i in range(B):
            if A % (i + 1) == 0 and B % (i + 1) == 0:
                yak = i + 1
            else:
                continue

    else:
        for i in range(A):
            if A % (i + 1) == 0 and B % (i + 1) == 0:
                yak = i + 1
            else:
                continue

    return yak

def solveBae(A, B):
    bae = 0

    if A < B:
        for i in range(B):
            if bae != 0:
                break
            else:
                for j in range(i, B):
                    if B * (i + 1) == A * (j + 1):
                        bae = A * (j + 1)
                        break
                    else:
                        continue

    else:
        for i in range(A):
            if bae != 0:
                break
            else:
                for j in range(i, A):
                    if A * (i + 1) == B * (j + 1):
                        bae = B * (j + 1)
                        break
                    else:
                        continue

    return bae

input = sys.stdin.readline

A, B = map(int, input().split())

print(solveYak(A, B))
print(solveBae(A, B))