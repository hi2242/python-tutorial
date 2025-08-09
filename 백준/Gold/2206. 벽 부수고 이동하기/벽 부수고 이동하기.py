import sys
from collections import deque

input = sys.stdin.readline

# [0] 기본 정보
# 맵(N * M)에서 0은 이동 가능, 1은 이동 불가능한 벽
# (1, 1) -> (N, M)으로 최단 경로로 이동
# 벽을 부숴서 경로가 짧아지면 하나까진 부술 수 있음
# 단, 시작하는 칸과 끝나는 칸도 카운트
def print_grid(array):
    for row in array:
        print(*row)

# [1] 이동
# 상하좌우 (-1, 0), (1, 0), (0, -1), (0, 1)로 이동 가능

# [2] 벽 부수기
# 최대 1회 가능

def bfs():
    visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
    d = deque()

    d.append((0, 0, True))
    visited[0][0][0] = 1

    while d:
        cr, cc, chance = d.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = cr + dr, cc + dc

            if 0 <= nr < N and 0 <= nc < M:
                if chance == True:
                    if grid[nr][nc] == 1:
                        d.append((nr, nc, False))
                        visited[nr][nc][1] = visited[cr][cc][0] + 1

                    elif visited[nr][nc][0] == 0:
                        d.append((nr, nc, True))
                        visited[nr][nc][0] = visited[cr][cc][0] + 1
                else:
                    if grid[nr][nc] == 1:
                        continue

                    elif visited[nr][nc][1] == 0:
                        d.append((nr, nc, False))
                        visited[nr][nc][1] = visited[cr][cc][1] + 1

    return visited[N - 1][M - 1]

def solve():
    answer = bfs()

    if answer == [0, 0]:
        print(-1)

    elif min(answer) == 0:
        print(max(answer))

    else:
        print(min(answer))

# 입력
# N(행), M(열)
# 맵의 정보
# 단, (1, 1), (N, M)은 항상 0
# 단, 1 <= N <= 1000, 1 <= M <= 1000
N, M = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(N)]

# 출력
# 최단 거리 (불가능할 땐 -1)
solve()