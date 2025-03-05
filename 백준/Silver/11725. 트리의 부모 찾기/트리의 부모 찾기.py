# 1이 없는 노드가 나오면 둘 중에 누가 부모인지 알 수 없으므로
# 양방향의 그래프를 만든 후 노드들을 저장하여 BFS를 통해
# 루트인 1부터 자식 노드를 찾아가는 방법을 채택해야 한다.

# 경우의 수를 하나하나 따져서 하면 양쪽 방향을 모두 비교 후 1을 찾기 때문에
# 시간 복잡도에서 손해가 발생한다.
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
d = deque()
temp = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    x, y = map(int, input().split())
    temp[x].append(y)
    temp[y].append(x)

def solve(graph):
    result = [0] * (N + 1)
    
    d.append(1)

    while d:
        current = d.popleft()
        for next in graph[current]:
            if result[next] == 0:
                result[next] = current
                d.append(next)
                

    return result

answer = solve(temp)

for i in range(2, N + 1):
    print(answer[i])

