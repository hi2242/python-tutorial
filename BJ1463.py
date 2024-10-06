import sys

input = sys.stdin.readline

N = int(input())
# DP문제에서 특징은 이전 단계에서 했던 내용을 기억한다는 것이다.
# DP(동적 프로그래밍)로 이전 단계를 기억하여 최적의 횟수를 찾아가는 문제이다.
# bottomup방식으로 2를 만드는 최적 횟수, 3을 만드는 최적 횟수 ...이런식으로
# 접근하여 원하는 N을 만드는 최적 횟수가 곧 N을 1로 만드는 최적 횟수와 같다.
d = [0] * (N + 1)

for i in range(2, N + 1):
    # 항상 가능한 "1을 뺀다."로 기본 횟수로 설정
    d[i] = d[i - 1] + 1

    # 항상 가능한 "1을 뺀다."와 "X가 2로 나누어 떨어지면, 2로 나눈다."를
    # 비교하여 더 최적의 횟수를 저장
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)


    # 이전까지 저장된 최적의 횟수와 "X가 3으로 나누어 떨어지면, 3로 나눈다."를
    # 비교하여 더 최적의 횟수를 저장
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)


print(d[N])

# import sys
# from collections import deque

# # 재귀함수에서 최종적으로 값을 return 받으려면 return을 붙여야된다.
# # 매 호출마다 print만 하고 return 받지않는다면 return을 붙이지 않아도 된다.
# # bfs를 적용한 풀이로 덱에서 하나씩 꺼내 횟수를 측정한다.
# # 최적 횟수를 출력하기 위해 visited를 이용하여 풀이한다.
# input = sys.stdin.readline

# N = int(input())

# visited = [0] * (N + 1)

# def solve():
#     d = deque()
#     d.append(N)

#     while d:
#         popD = d.popleft()

#         if popD == 1:
#             break

#         if visited[popD // 3] == 0 and popD % 3 == 0:
#             visited[popD // 3] = visited[popD] + 1
#             d.append(popD // 3)

#         if visited[popD // 2] == 0 and popD % 2 == 0:
#             visited[popD // 2] = visited[popD] + 1
#             d.append(popD // 2)

#         if visited[popD - 1] == 0:
#             visited[popD - 1] = visited[popD] + 1
#             d.append(popD - 1)

# solve()
# print(visited[1])