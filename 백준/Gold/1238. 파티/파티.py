import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

# [0] 기본 정보
# N개의 숫자로 구분된 마을에 학생이 한명씩 존재
# 마을 사이에는 총 M개의 단방향 도로 존재 (i번째 길을 지나는데 Ti 시간 소모)
# 각 학생들은 X번 마을에 모여 파티하고 돌아감 (최단 경로)
# 가장 많은 시간을 소비하는 학생 찾기
def dijkstra_fir(start):
    result = [INF for _ in range(N + 1)]
    heap = []
    cost = 0

    heapq.heappush(heap, (cost, start))

    while heap:
        curr_cost, curr_pos = heapq.heappop(heap)

        for d_end, d_cost in road_info[curr_pos]:
            if result[d_end] == INF or result[d_end] > curr_cost + d_cost:
                result[d_end] = curr_cost + d_cost
                heapq.heappush(heap, (d_cost + curr_cost, d_end))

    return result

def dijkstra_sec(start, end):
    visited = [0 for _ in range(N + 1)]
    heap = []
    cost = 0

    heapq.heappush(heap, (cost, start))

    while heap:
        curr_cost, curr_pos = heapq.heappop(heap)

        if curr_pos == end:
            return curr_cost

        for d_end, d_cost in road_info[curr_pos]:
            if visited[d_end] == 0 or visited[d_end] > curr_cost + d_cost:
                visited[d_end] = d_cost + curr_cost
                heapq.heappush(heap, (d_cost + curr_cost, d_end))

    return INF


    
def solve():
    answer = [0 for _ in range(N + 1)]

    result = dijkstra_fir(X)
    
    for i in range(1, N + 1):
        answer[i] += dijkstra_sec(i, X)
        answer[i] += result[i]
        
    return max(answer)

# [1] 각 도시 -> 파티 장소

# [2] 파티 장소 -> 각 도시

# 입력
# N(마을의 수), M(도로의 수), X(파티 장소)
# i번째 도로의 정보 (시작점, 끝점, 소요시간)
# 단, 시작점 == 끝점인 도로는 없음
# 단, 시작점과 끝점을 잇는 도로는 최대 1개
# 단, 모든 마을에서 X까지는 갈 수도 있고 돌아올 수도 있음
N, M, X = map(int, input().split())
road_info = {i : [] for i in range(N + 1)}
    
for _ in range(M):
    start, end, cost = map(int, input().split())
    road_info[start].append((end, cost))

# 출력
# 가장 오래걸리는 학생의 소요시간
print(solve())