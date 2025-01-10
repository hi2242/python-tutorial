# 분할 정복법에 관한 문제로 주어진 문제를 사례(해당 문제에서는 1사분면부터 4사분면)로 나누고
# 각각의 작은 문제들을 해결하여 정복한다.
import sys

input = sys.stdin.readline

length = int(input())
graph = []
blueCount = 0
whiteCount = 0

graph = [list(map(int, input().split())) for _ in range(length)]
# for i in range(length):
#     grid = list(map(int, input().split()))
#     graph.append(grid)

def cutting(x, y, N):
    global blueCount, whiteCount
    color = graph[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != graph[i][j]:
                cutting(x, y, N // 2)
                cutting(x, y + N // 2, N // 2)
                cutting(x + N // 2, y, N // 2)
                cutting(x + N // 2, y + N // 2, N // 2)
                return
            
    if color == 0:
        whiteCount += 1

    else:
        blueCount += 1

cutting(0, 0, length)
print(whiteCount, blueCount, sep = '\n')
