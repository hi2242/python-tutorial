# lambda 정렬을 통해 오름차순, 내림차순으로 정렬할 수 있다.
# 1. 2차원 배열 오름차순 정렬 사용 예시
# arr.sort(key = lambda x : (x[1], x[0]))
# -> 2차원 배열의 각 인덱스 1번째 요소로 오름차순 정렬 후 동일하면 0번째 요소로 오름차순 정렬

# 2. 2차원 배열 내림차순 정렬 사용 예시
# arr.sort(key = lambda x : (x[0], -x[1]))
# ->2차원 배열의 각 인덱스 0번째 요소로 오름차순 정렬 후 동일하면 1번째 요소로 내름차순 정렬

# 회의를 종료 시각 기준으로 정렬하여 가장 먼저 끝나는 회의를 기준으로
# 그 종료 시간 이후 가장 빨리 시작하는 회의이면서 가장 빨리 끝나는 회의를
# 선택할 수 있다.
import sys

input = sys.stdin.readline

N = int(input())

grid = []

for i in range(N):
    start, end = map(int, input().split())
    grid.append((start, end))

grid.sort(key=lambda x: (x[1], x[0]))

count = 0
newEnd = 0

for start, end in grid:
    if newEnd <= start:
        newEnd = end
        count += 1

print(count)