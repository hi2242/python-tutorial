import sys
from collections import deque

input = sys.stdin.readline

def print_grid(array):
    for row in array:
        print(*row)

# [0] 기본 정보
# 트리 : 사이클이 없는 무방향 그래프
# 두 노드의 사이 경로는 하나만 존재
# 트리의 지름 : 가장 경로가 긴 두 노드가 이루는 원의 지름

# [1] 트리 생성
def init(p, c, w):
    tree[p].append((c, w))
    tree[c].append((p, w))

# [2] 시작점으로부터 거리
def calc_dist(start):
    dist_arr = [0 for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]

    d = deque()
    d.append(start)
    visited[start] = 1
    
    while d:
        curr = d.popleft()

        if tree[curr]:
            for dest, weight in tree[curr]:
                if visited[dest] == 0:
                    dist_arr[dest] = dist_arr[curr] + weight
                    d.append(dest)
                    visited[dest] = 1

    return dist_arr

def solve():
    distance = calc_dist(1)
    result = calc_dist(distance.index(max(distance)))

    return max(result)

    

# 입력
# n(노드의 개수)
# u(부모 노드), v(자식 노드), w(가중치)
# 단, 부모 노드의 번호가 작은 것이 먼저 입력되고 같으면 자식 노드의 번호가 작은 것이 입력
# 단, 1 <= n <= 10000
# 단, 루트 노드의 번호 : 1
# 단, w <= 100 인 양의 정수
n = int(input())
tree = {i: [] for i in range(n + 1)}
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    init(u, v, w)

# 출력
# 트리의 지름
print(solve())