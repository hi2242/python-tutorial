import sys

input = sys.stdin.readline

# 계수 정렬

N = int(input())

arr = [0] * 10000

for _ in range(N):
    arr[int(input()) - 1] += 1

for i in range(10000):
    if N == 0:
        break
    for _ in range(arr[i]):
        print(i + 1)
        N -= 1