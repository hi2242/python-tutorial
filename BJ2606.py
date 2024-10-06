# dfs, bfs = 경로탐색, 타겟 넘버, 네트워크, 조합 유형
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

grid = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

M = int(input())

for _ in range(M):
    a, b = map(int, input().split())

    grid[a].append(b)
    grid[b].append(a)
 
def solve():
    d = deque()
    count = 0

    d.append(1)
    visited[1] = 1

    while d:
        nextCom = d.popleft()
        for i in grid[nextCom]:
            if not visited[i]:
                d.append(i)
                visited[i] = 1
                count += 1

    return count


print(solve())