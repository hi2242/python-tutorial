# [0] 기본 조건
# 정수 삼각형에서 아래층으로 내려오면서 합이 최대가 되도록 경로를 정함
# 대각선 왼쪽 또는 대각선 오른쪽으로만 이동 가능
# 단, 각 정수의 범위는 0 이상 9999 이하이다.

# [1] DP
# dp[i][j] = max(dp[i - 1][j] + tri[i][j], dp[i - 1][j + 1] + tri[i][j])

def print_grid(array):
    for row in array:
        print(*row)

    print()

def init():
    dp[0][0] = tri[0][0]

    for i in range(1, N):
        dp[i][0] = dp[i - 1][0] + tri[i][0]

def solve():
    init()

    for i in range(1, N):
        for j in range(1, i + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + tri[i][j], dp[i - 1][j] + tri[i][j])

# 입력
# 삼각형의 크기 N (1 <= N <= 500)
# N + 1번째 줄까지 정수 삼각형이 주어진다.
N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

# 출력
# 합이 최대가 되는 경로의 합
solve()
print(max(dp[N - 1]))