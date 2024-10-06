import sys
from collections import deque

def solve(n):
    d = deque([0, 1])

    if N == 1:
        print(1, 0)

    else:
        for _ in range(N - 1):
            d.append(d.popleft() + d[0])
        print(d[0], d[1])

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    solve(N)

# # dp를 이용한 풀이 방법

# import sys

# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     N = int(input())
    
#     # 0, 1의 호출 횟수(N은 40보다 작거나 같은 자연수 또는 0)
#     zero = [0] * 41
#     one = [0] * 41

#     zero[0], one[0] = 1, 0
#     zero[1], one[1] = 0, 1

#     for i in range(2, N + 1):
#         zero[i] = zero[i - 1] + zero[i - 2]
#         one[i] = one[i - 1] + one[i - 2]

#     print(zero[N], one[N])