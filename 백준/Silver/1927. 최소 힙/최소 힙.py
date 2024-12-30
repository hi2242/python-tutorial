import sys
import heapq
# heapq는 최소힙(min-heap)을 구현한 모듈이다.
# 파이썬에서 &는 비트연산자이고 and는 논리연산자이다.
input = sys.stdin.readline

inputN = int(input())

heap = []
output = []

for i in range(inputN):
    x = int(input())
    if x == 0 and len(heap) == 0:
        output.append(0)
    elif x == 0:
        output.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)

print("\n".join(map(str, output)))