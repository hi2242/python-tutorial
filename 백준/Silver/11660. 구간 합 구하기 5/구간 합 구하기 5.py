import sys

input = sys.stdin.readline

# [0] 기본 조건
# 표(N * N)에서 (x1, y1) ~ (x2, y2)에 해당하는 칸의 합 (행, 열)

# [1] DP 초기화
def init():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            dp[r][c] = grid[r - 1][c - 1] + dp[r - 1][c] + dp[r][c - 1] - dp[r - 1][c - 1]

# [2] 칸의 합
def table_sum(x1, y1, x2, y2):
    return dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]

# 입력
# N(표의 크기), M(합을 구해야하는 횟수)
# 크기가 N * N인 표의 정보
# 합을 구해야하는 정보
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

init()

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(table_sum(x1, y1, x2, y2))

# 출력