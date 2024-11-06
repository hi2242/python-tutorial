# bfs 알고리즘에 대한 문제이다.
import sys
# bfs에 대한 알고리즘은 deque을 import하여 사용한다.
from collections import deque

input = sys.stdin.readline

def solve(graph, x, y):
    d = deque()
    d.append((x, y))
    # 입력받은 그래프에서 지나간 자리는 0으로 만든다.
    graph[x][y] = 0

    # deque이 비어있으면 더이상 전진할 수 없다는 의미이다.
    while d:
        x, y = d.popleft()

        # 주변을 탐색하는 반복문을 넣는다.
        # dx와 dy는 상, 하, 좌, 우 등 본문에서 알맞게 리스트로 정의한다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 주변을 탐색하는데 각 테두리에서는 overflow가 발생할 수 있기 때문에 조건문을 이용한다.
            # 아직 지나가지 않은 자리로 이동한 다음 그것을 deque에 다시 넣고 지나갔다는 0 표시를 한다.
            if 0 <= nx < rowLength and 0 <= ny < columnLength and grid[nx][ny] == 1:
                d.append((nx, ny))
                grid[nx][ny] = 0

    return



testCaseT = int(input())

for _ in range(testCaseT):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    result = 0
    rowLength, columnLength, locationCount = map(int, input().split())
    # 행렬은 column을 먼저 만들고 반복문으로 row를 만들어서 2차원 배열을 완성한다.
    grid = [[0] * columnLength for _ in range(rowLength)]

    # 주어진 지도를 그린다.
    for _ in range(locationCount):
        rowX, columnY = map(int, input().split())
        grid[rowX][columnY] = 1

    # 지도를 처음부터 끝까지 돌면서 시작점(1)을 찾는다면 bfs를 실행하고 카운트를 1 올린다.
    for i in range(rowLength):
        for j in range(columnLength):
            if grid[i][j] == 1:
                solve(grid, i, j)
                result += 1
    print(result)