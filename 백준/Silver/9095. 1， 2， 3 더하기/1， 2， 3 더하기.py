# 동적 프로그래밍 dp 문제
import sys
from collections import deque

input = sys.stdin.readline

def solve(x):
    dp = [0] * (x + 1)

    for i in range(1, x + 1):
        if i == 1:
            dp[i] = 1

        elif i == 2:
            dp[i] = 2

        elif i == 3:
            dp[i] = 4

        else:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[x]

testNum = int(input())

for _ in range(testNum):
    testCase = int(input())
    print(solve(testCase))

# import sys
# from collections import deque

# input = sys.stdin.readline

# def solve(x):
#     count = 0
#     d = deque([0])

#     while d:
#         current = d.popleft()

#         if current == x:
#             count += 1
#             continue
        
#         for step in [1, 2, 3]:
#             if current + step <= x:
#                 d.append(current + step)

#     print(count)

# testNum = int(input())

# for _ in range(testNum):
#     testCase = int(input())
#     solve(testCase)

