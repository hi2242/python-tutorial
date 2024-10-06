import sys
#import queue
from collections import deque

input = sys.stdin.readline

N = int(input())

q = deque([])
for i in range(N):
    q.append(i + 1)

for _ in range(N):
    if len(q) == 1:
        print(q.popleft())

    else:
        q.popleft()
        q.append(q.popleft())
