import sys

input = sys.stdin.readline

N = int(input())

rowA = set(map(int, input().split()))

M = int(input())

rowM = list(map(int, input().split()))

for i in range(M):
    if rowM[i] in rowA:
        print("1")

    else:
        print("0")
