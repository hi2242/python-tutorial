import sys
from collections import deque

input = sys.stdin.readline

# [0] 기본 정보
# 트리의 지름 : 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것
def print_grid(array):
    for row in array:
        print(*row)
        
def solve(start):
    visited = [0 for _ in range(V + 1)]
    
    d = deque()
    d.append((start, 0))
    answer = index = 0
    visited[start] = 1

    while d:
        cp, cost = d.popleft()

        if answer < cost:
            answer = cost
            index = cp

        for np, weight in grid[cp]:
            if visited[np] == 0:
                d.append((np, cost + weight))
                visited[np] = 1

    return answer, index

# 입력
# V(정점 개수)
# 간선의 정보 (시작 정점 번호, (도착 정점 번호, 정점까지의 거리), -1)
# 단, 2 <= V <= 100000
# 단, 거리 <= 10000인 자연수
V = int(input())
grid = {i : [] for i in range(1, V + 1)}

for _ in range(V):
    edge = list(map (int, input().split()))
    for i in range(1, len(edge) // 2):
        grid[edge[0]].append((edge[2 * i - 1], edge[2 * i]))

# 출력
# 트리의 지름
temp, index = solve(1)
answer, index = solve(index)
print(answer)