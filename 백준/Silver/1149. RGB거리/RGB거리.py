# 몇개 안되는 개수에도 최소/최대를 계산할 때 시간 복잡도 이슈가 생긴다면 DP 풀이를 채택
# 최종 결과를 위해 계산을 할 때 같은 연산을 반복한다면 DP 풀이를 채택
# DP란 이미 사용한 이전 내용을 버리고 계속 최적화된 값을 업데이트하면서 앞으로만 진행하는 알고리즘

import sys

input = sys.stdin.readline

N = int(input())
rgb = []

for _ in range(N):
    rgb.append(list(map(int, input().split())))

def solve(count, home):
    for i in range(1, count):
        home[i][0] += min(home[i - 1][1], home[i - 1][2])
        home[i][1] += min(home[i - 1][0], home[i - 1][2])
        home[i][2] += min(home[i - 1][0], home[i - 1][1])

    return min(home[count - 1])

result = solve(N, rgb)

print(result)