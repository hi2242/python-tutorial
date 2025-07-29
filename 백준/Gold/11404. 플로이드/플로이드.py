import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# [0] 기본 정보
# N개의 도시 중 한 도시에서 출발하여 다른 도시에 도착하는 버스 M개가 있음
# 모든 도시의 쌍 (A, B)에 대해서 필요한 비용의 최솟값 구하기

def print_grid(array):
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            print(array[r][c], end = " ")

        print()

def result():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if graph[r][c] == INF:
                graph[r][c] = 0

# [1] 그래프 만들기
# 딕셔너리로 시작 인덱스에 도착 지점과 비용 정보 저장
# 최소 비용으로 갱신

# [2] 시작점으로부터 최소 비용 갱신
# 플로이드 알고리즘을 통해 출발지 -> 도착지를 직접 가는 것과
# 경유해서 가는 것을 비교하여 O(N^3)의 시간을 사용해 최소 비용 행렬을 만듦
def solve():
    for stop in range(1, N + 1):
        for start in range(1, N + 1):
            for end in range(1, N + 1):
                graph[start][end] = min(graph[start][end], graph[start][stop] + graph[stop][end])

    result()

# 입력
# N(도시의 개수)
# M(버스의 개수)
# a, b, c (버스 정보 : 시작 도시, 도착 도시, 비용)
# 단, 시작과 도착 도시가 같은 경우는 없음
# 단, 2 <= N <= 100, 1 <= m <= 100000
# 단, 비용은 100000보다 작거나 같은 자연수
# 단, 시작과 도착을 연결하는 노선은 여러 개 일 수 있음
N = int(input())
M = int(input())
graph_dict = {i: [] for i in range(N + 1)}

graph = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N):
    graph[i + 1][i + 1] = 0

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph_dict[start].append((end, cost))
    graph[start][end] = min(graph[start][end], cost)

# 출력
# 행렬로 비용을 보여줌
# 단, i에서 j로 못가는 경우엔 0을 출력
solve()
print_grid(graph)