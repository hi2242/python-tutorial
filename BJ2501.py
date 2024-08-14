import sys

input = sys.stdin.readline

N, K = map(int, input().split())

for i in range(N):
    if N % (i + 1) == 0:
        K -= 1
        if K == 0:
            print(i + 1)
            break
        
        elif i == (N - 1) and K != 0:
            print(0)
            break
        
        else:
            continue

    else:
        continue