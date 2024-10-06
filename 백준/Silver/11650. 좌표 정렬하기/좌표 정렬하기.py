import sys

input = sys.stdin.readline

N = int(input())

grid = []

for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

sortGrid = sorted(grid, key = lambda x : (x[0], x[1]))

for x in sortGrid:
    print(' '.join(map(str, x)))