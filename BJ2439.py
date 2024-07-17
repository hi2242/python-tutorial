import sys
input = sys.stdin.readline

N = int(input())

for i in range(0, N):
    for j in range(N - (i + 1), 0, -1):
        print(" ", end = "")

    for j in range(0, i + 1):
        print("*", end = "")

    print("")