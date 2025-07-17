import sys
from collections import deque

input = sys.stdin.readline

# [0] 기본 정보
# 수빈의 위치 N, 동생의 위치 K
# 수빈이는 걷거나 순간이동 가능
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지
def solve():
    visited = [0 for _ in range(100001)]

    d = deque()
    d.append(N)
    visited[N] = 1

    while d:
        cp = d.popleft()
        
        for dp in [1, -1, cp]:
            np = cp + dp

            if 0 <= np < 100001:
                if visited[np]:
                    if dp != cp and road[np] > road[cp] + 1:
                        d.append(np)
                        road[np] = road[cp] + 1

                    elif dp == cp and road[np] > road[cp]:
                        d.append(np)
                        road[np] = road[cp]

                else:
                    visited[np] = 1
                    d.append(np)
                    if dp != cp:
                        road[np] = road[cp] + 1
                    else:
                        road[np] = road[cp]


# [1] 수빈이의 걷기
# 위치 X에서 1초 후에 X-1 또는 X+1로 이동 가능

# [2] 수빈이의 순간이동
# 위치 X에서 0초 후에 2*X로 이동 가능

# 입력
# N(수빈이의 위치), K(동생의 위치)
# 단, 0 <= N <= 100000, 0 <= K <= 100000
N, K = map(int, input().split())
road = [0 for _ in range(100001)]

# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간
solve()
print(road[K])