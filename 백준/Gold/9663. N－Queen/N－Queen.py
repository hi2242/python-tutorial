import sys

input = sys.stdin.readline

# [0] 기본 정보
# 체스판(N * N) 위에 퀸 N개를 서로 공격할 수 없게 놓음

# [1] 가능한 위치 찾기            
def possible(r):
    global answer

    if r == N:
        answer += 1
        return
    
    for c in range(N):
        if not visited[c] and not right[r - c + (N - 1)] and not left[r + c]:
            visited[c] = right[r - c + (N - 1)] = left[r + c] = True
            possible(r + 1)
            visited[c] = right[r - c + (N - 1)] = left[r + c] = False

# 입력
# N
# 단, 1 <= N < 15
N = int(input())
visited = [False for _ in range(N)]
right = [False for _ in range(2 * N - 1)]
left = [False for _ in range(2 * N - 1)]

answer = 0

# 출력
# 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수
possible(0)
print(answer)