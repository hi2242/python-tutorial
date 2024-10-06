import sys
from collections import deque
# 큐만을 이용해서는 값을 조회만 할 수 없으므로 덱이나 리스트를 사용한다.

input = sys.stdin.readline

N = int(input())
d = deque()

for _ in range(N):
    command = list(input().split())
    if command[0] == "push":
        d.append(command[1])
    elif command[0] == "pop":
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif command[0] == "size":
        print(len(d))
    elif command[0] == "empty":
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif command[0] == "back":
        if len(d) == 0:
            print(-1)
        else:
            print(d[len(d) - 1])
    else:
        continue