import sys

input = sys.stdin.readline

T = int(input())
B = []

for i in range(0, T):
    A = str(input())
    C = len(A) - 1
    B.append(A[0] + A[C - 1])

for i in range(0, T):
    print(B[i])