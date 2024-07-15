import sys

input = sys.stdin.readline

W = list(map(int, input().split()))

B = [1, 1, 2, 2, 2, 8]

for i in range(0, 6):
    print(B[i] - W[i], end = " ")