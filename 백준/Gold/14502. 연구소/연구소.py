import sys
from collections import deque
import copy
from itertools import combinations

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

def print_grid(grid):
    for row in grid:
        print(*row)

def wall_virus_count(grid):
    d = deque()
    v = deque()

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                d.append((i, j))

            elif grid[i][j] == 2:
                v.append((i, j))

    return d, v

def bfs(grid, virus):
    visited = [[0 for _ in range(M)] for _ in range(N)]

    d = deque()

    for each in virus:
        d.append(each)
        visited[each[0]][each[1]] = 1

    while d:
        cr, cc = d.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = cr + dr, cc + dc

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and grid[nr][nc] == 0:
                visited[nr][nc] = 1
                grid[nr][nc] = 2
                d.append((nr, nc))

    return grid

def solve():
    d, virus = wall_virus_count(arr)
    largest = 0
    
    for x, y, z in combinations(d, 3):
        temp = copy.deepcopy(arr)
        temp[x[0]][x[1]] = 1
        temp[y[0]][y[1]] = 1
        temp[z[0]][z[1]] = 1

        result = bfs(temp, virus)

        d, v = wall_virus_count(result)

        if largest < len(d):
            largest = len(d)

    return largest

N, M = map(int, input().split())

arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

print(solve())