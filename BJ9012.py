import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

count = 0
result = []

for i in range(N):
    d = deque(input().rstrip())
    for _ in range(len(d)):
        if d.popleft() == "(":
            count += 1

        else:
            count -= 1

        if count < 0:
            result.append("NO")
            count = 0
            break

    else:
        if count == 0:
            result.append("YES")
            count = 0

        else:
            result.append("NO")
            count = 0

    
print("\n".join(map(str, result)))