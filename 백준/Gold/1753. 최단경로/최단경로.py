import sys
import heapq

input = sys.stdin.readline

# [0] 기본 정보
# 주어진 시작점에서 다른 모든 정점으로의 최단 경로
# 모든 간선의 가중치는 10 이하의 자연수

# [1] 그래프 만들기
# 딕셔너리를 통해 u: (v, w)
# 두 정점에 대해 간선이 여러개이면 최소값으로 갱신
def init(start, end, weight):
    graph[start].append((end, weight))


# [2] 최단 경로 계산하기
# 시작점을 입력받아 각 정점마다의 최소값 계산
def solve(start):
    result = ["INF" for _ in range(V + 1)]
    heap = []
    heapq.heappush(heap, (0, start))
    result[start] = 0

    while heap:
        cost, curr = heapq.heappop(heap)

        for end, weight in graph[curr]:
            if result[end] == "INF":
                result[end] = cost + weight
                heapq.heappush(heap, (cost + weight, end))

            elif result[end] > cost + weight:
                result[end] = cost + weight
                heapq.heappush(heap, (cost + weight, end))

    return result

# 입력
# V(정점의 개수), E(간선의 개수)
# K(시작 정점의 번호)
# u, v, w (u에서 v로 가는 가중치 w)
# 단, 1 <= V <= 20000, 1 <= E <= 300000
# 단, 모든 정점에는 1부터 V까지 번호가 매겨져있다.
# 단, 1 <= K <= V
# 단, u != v, w <= 10
# 단, 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음
V, E = map(int, input().split())
K = int(input())
# graph = dict(zip([i for i in range(1, V + 1)], [[] for _ in range(1, V + 1)]))
graph = {i: [] for i in range(1, V + 1)}
for _ in range(E):
    u, v, w = map(int ,input().split())
    init(u, v, w)

# 출력
# V 줄에 걸쳐 i번째 줄에 i번 정점으로의 최단 경로의 경로값
# 단, 시작점 자신은 0으로 출력하고 경로가 없으면 INF로 출력
for i in solve(K)[1:V + 1]:
    print(i)