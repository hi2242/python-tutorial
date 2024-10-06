import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

d = deque()
S = []

for i in range(N):
    d.append(i + 1)

for _ in range(N):
    d.rotate(1 - K)
    S.append(d.popleft())

print("<" + ", ".join(map(str, S)) + ">")