import sys
from collections import deque

# BFS를 이용한 풀이
# 1. 방향이 없는 그래프이므로 2차원 배열에 서로를 저장
# 2. 시작점을 정하여 덱에 집어넣고 방문처리
# 3. 덱이 빌때까지 2차원 배열에서 꺼내서 방문 확인 후 덱에 다시 집어넣고 방문처리하는 BFS 메서드를 정의
# 4. 시작점을 정점 하나씩 대입하며 visited를 모두 방문처리 될 때까지 카운트
# 연결 요소는 섬 문제와 동일하게 독립된 점 또한 하나의 연결 요소이다.

input = sys.stdin.readline

connectionCount = 0

point, line = map(int, input().split())

connectionList = [[] for _ in range(point + 1)]
visited = [0] * (point + 1)

for _ in range(line):
    start, end = map(int, input().split())
    connectionList[start].append(end)
    connectionList[end].append(start)

def solve(start):
    d = deque()
    d.append(start)
    visited[start] = 1

    while d:
        start = d.popleft()
        for i in connectionList[start]:
            if visited[i] == 0:
                d.append(i)
                visited[i] = 1


for i in range(1, point + 1):
    if visited[i] == 0:
        solve(i)
        connectionCount += 1

print(connectionCount)