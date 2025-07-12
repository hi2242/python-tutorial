import sys
# [0] 기본 정보
# LCS : 두 수열의 공통 부분 수열 중 가장 긴 것
input = sys.stdin.readline

def solve():
    dp = [[0 for _ in range(count_M + 1)] for _ in range(count_N + 1)]
    for r in range(1, count_N + 1):
        for c in range(1, count_M + 1):
            if N[r - 1] == M[c - 1]:
                dp[r][c] = dp[r - 1][c - 1] + 1

            else:
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

    return dp[count_N][count_M]

# 입력
# 최대 1000글자의 알파벳 대문자 문자열 두 줄
M = input().rstrip()
N = input().rstrip()
count_M = len(M)
count_N = len(N)

# 출력
# LCS 길이
print(solve())