import sys
from collections import deque

input = sys.stdin.readline

pointX, pointY = map(int, input().split())
visited = [0] * 100001

timer = 0

d = deque()

d.append(pointX)
visited[pointX] = 1

def solve(pointY):
    global result
    result = deque()

    while d:
        X = d.popleft()
        visited[X] = 1

        if X * 2 == pointY or X - 1 == pointY or X + 1 == pointY:
            result.clear()
            break

        if 0 <= X * 2 < 100001 and visited[X * 2] == 0:
            result.append(X * 2)
            visited[X * 2] = 1

        if 0 <= X - 1 < 100001 and visited[X - 1] == 0:
            result.append(X - 1)
            visited[X - 1] = 1

        if 0 <= X + 1 < 100001 and visited[X + 1] == 0:
            result.append(X + 1)
            visited[X + 1] = 1


while d:
    if pointX == pointY:
        break
    solve(pointY)
    timer += 1
    d = result

print(timer)