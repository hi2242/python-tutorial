import sys
from collections import deque

input = sys.stdin.readline

# grid 출력 함수
def print_grid(grid):
    for row in grid:
        print(*row)

def bfs(shark_r, shark_c, shark_size):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    d = deque()
    fish_can_list = []
    nearest = 0

    d.append((shark_r, shark_c))
    visited[shark_r][shark_c] = 0

    while d:
        cr, cc = d.popleft()

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and shark_size >= arr[nr][nc]:
                d.append((nr, nc))
                visited[nr][nc] = visited[cr][cc] + 1
                if shark_size > arr[nr][nc] > 0:
                    fish_can_list.append((nr, nc))

    new_fish_list = []

    for r, c in fish_can_list:
        temp = visited[r][c]
        if nearest == 0:
            nearest = temp
        if nearest > temp:
            nearest = temp

    for r, c in fish_can_list:
        temp = visited[r][c]
        if nearest == temp:
            new_fish_list.append((r, c))
    return new_fish_list, visited

# 아기 상어 찾는 함수
def shark_find(grid):
    a, b = -1, -1
    for i in range(N):
        if 9 in grid[i]:
            a, b = i, grid[i].index(9)
            break

    return a, b

# 아기 상어가 먹는 함수
def shark_eat(fish_r, fish_c, shark_r, shark_c, shark_eat_count):
    # 보통은 BFS에서 본인에 대한 방문 여부를 1로 표기하는데 해당 문제에선 0으로 설정했으므로
    # arr[fish_r][fish_c] = 9로 상어를 표기해두면 자기 자신에 의해 경로가 막히는 경우가 생긴다.
    arr[fish_r][fish_c] = 0
    arr[shark_r][shark_c] = 0
    shark_r, shark_c = fish_r, fish_c

    return shark_r, shark_c, shark_eat_count + 1

def solve():
    shark_size, shark_eat_count, time_count = 2, 0, 0
    shark_r, shark_c = shark_find(arr)

    while True:
        fish_can_list, visited = bfs(shark_r, shark_c, shark_size)

        if len(fish_can_list) == 0:
            break
        fish_can_list.sort(key=lambda x: (x[0], x[1]))
        fish_r, fish_c = fish_can_list[0]
        dist = visited[fish_r][fish_c]

        shark_r, shark_c, shark_eat_count = shark_eat(fish_r, fish_c, shark_r, shark_c, shark_eat_count)

        time_count += dist
        if shark_size == shark_eat_count:
            shark_size += 1
            shark_eat_count = 0

    return time_count

# 입력
# 공간의 크기 N
N = int(input())

# 공간의 상태 N줄
arr = []
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

print(solve())