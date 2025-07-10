# [0] 기본 정보
# 스티커 2n개를 2행 n열로 배치

# [1] 스티커 떼기
# 스티커를 떼면 변을 공유하는 상하좌우도 못쓰게 된다.
# 스티커의 합이 최대가 되도록 뗀다.
def print_grid(array):
    for row in array:
        print(*row)

    print()

def DP(table, k):
    dp = [[0 for _ in range(k + 2)] for _ in range(2)]

    for cc in range(2, k + 2):
        for cr in range(2):
            if cr == 0:
                dp[cr][cc] = max(dp[cr + 1][cc - 2], dp[cr + 1][cc - 1]) + table[cr][cc - 2]

            elif cr == 1:
                dp[cr][cc] = max(dp[cr - 1][cc - 2], dp[cr - 1][cc - 1]) + table[cr][cc - 2]

    print(max(dp[0][k + 1], dp[1][k + 1]))
    
# 입력
T = int(input())
for _ in range(T):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(2)]
    DP(grid, n)

# 출력
