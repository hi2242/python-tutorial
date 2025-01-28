import sys
from collections import deque

input = sys.stdin.readline

def solve(grid, path, visited, x, y):
    d = deque()
    d.append((x, y))
    visited[x][y] = 1
    path[x][y] = 0

    while d:
        x, y = d.popleft()
        count = path[x][y]
        
        count += 1
        for i in range(4):
            afterX = x + moveX[i]
            afterY = y + moveY[i]

            if 0 <= afterX < vertical and 0 <= afterY < horizontal and grid[afterX][afterY] == 0:
                visited[afterX][afterY] = -1
                path[afterX][afterY] = 0

            elif 0 <= afterX < vertical and 0 <= afterY < horizontal and visited[afterX][afterY] == 0:
                d.append((afterX, afterY))
                visited[afterX][afterY] = 1
                path[afterX][afterY] = count

    for row in path:
        print(' '.join(map(str, row)))



grid = []
moveX = [1, -1, 0, 0]
moveY = [0, 0, 1, -1]

vertical, horizontal = map(int, input().split())

visited = [[0] * horizontal for _ in range(vertical)]
path = [[-1] * horizontal for _ in range(vertical)]

for i in range(vertical):
    row = list(map(int, input().split()))
    grid.append(row)

for i in range(vertical):
    for j in range(horizontal):
        if grid[i][j] == 2:
            startX, startY = i, j

        if grid[i][j] == 0:
            path[i][j] = 0

solve(grid, path, visited, startX, startY)


