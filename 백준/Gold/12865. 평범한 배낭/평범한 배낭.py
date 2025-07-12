import sys

input = sys.stdin.readline

# [0] 기본 정보
# 최대한 가치 있는 배낭 만들기
# N개의 물건 중 무게 제한 K 이내로 선택하여 가치를 최대치로 함
# 각 물건은 W의 무게와 V의 가치를 지님
def solve():
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for r in range(1, N + 1):
        for c in range(1, K + 1):
            if c >= product[r - 1][0]:
                dp[r][c] = max(dp[r - 1][c], product[r - 1][1] + dp[r - 1][c - product[r - 1][0]])

            else:
                dp[r][c] = dp[r - 1][c]

    return dp[N][K]

# 입력
# N(물품의 수), K(무게 제한)
# 각 물건의 W(무게), V(가치)
# 단, 각 입력은 정수이다.
# 1 <= N <= 100
# 1 <= K <= 100000
# 1 <= W <= 100000
# 0 <= V <= 1000
N, K = map(int, input().split())
product = [list(map(int, input().split())) for _ in range(N)]

# 출력
# 가치합의 최대값
print(solve())