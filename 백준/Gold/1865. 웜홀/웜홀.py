import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)

# [0] 기본 정보
# N개의 지점 사이에 M개의 도로와 W개의 웜홀
# 단, 도로는 방향이 없고 웜홀은 방향이 있음
# 웜홀 : 시작 위치 -> 도착 위치 (걸리는 시간이 음수)
# 출발지로 다시 되돌아 왔을 때 시간이 오히려 이전이 되는 경우를 찾기

# [1] 프로그램 정보
# 음의 가중치가 있으므로 더이상 갱신이 안될때까지 갱신 (완전탐색)
# 덱 사용
def solve(N, city_info):

    count = [0 for _ in range(N + 1)]
    dist = [0 for _ in range(N + 1)]
    in_deque = [False for _ in range(N + 1)]
    
    d = deque()

    for i in range(1, N + 1):
        d.append(i)
        in_deque[i] = True

    while d:
        curr_pos = d.popleft()
        in_deque[curr_pos] = False

        for next_pos, next_cost in city_info[curr_pos]:
            if dist[next_pos] > dist[curr_pos] + next_cost:
                count[next_pos] += 1
                dist[next_pos] = dist[curr_pos] + next_cost
                
                if count[next_pos] >= N:
                    return "YES"
                
                if not in_deque[next_pos]:
                    d.append(next_pos)
                    in_deque[next_pos] = True

    return "NO"

# 입력
# TC(테스트 케이스)
# N(지점의 수), M(도로의 개수), W(웜홀의 개수)
# 도로 정보 S, E, T (S, E : 연결 지점의 번호, T : 걸리는 시간)
# 웜홀 정보 S, E, T (S, E : 연결 지점의 번호, T : 걸리는 시간)
# 단, 1 <= TC <= 5
# 단, 1 <= N <= 500, 1 <= M <= 2500, 1 <= W <= 200
# 단, T는 10000보다 작거나 같은 자연수 또는 0
# 단, 두 지점을 연결하는 도로는 한 개보다 많을 수 있음
TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    city_info = {i : [] for i in range(N + 1)}

    for _ in range(M):
        S, E, T = map(int, input().split())
        if S != E:
            city_info[E].append((S, T))
        city_info[S].append((E, T))

    for _ in range(W):
        S, E, T = map(int, input().split())
        city_info[S].append((E, -T))

    for i in range(1, N + 1):
        city_info[i].sort(key = lambda x : (x[1], x[0]))

    print(solve(N, city_info))

# 출력
# 각 TC마다 시간이 줄어들게 출발 위치로 돌아오면 YES, 안되면 NO