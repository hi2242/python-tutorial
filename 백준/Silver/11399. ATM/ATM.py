import sys

input = sys.stdin.readline

N = int(input())
count = 0

atmTime = list(map(int, input().split()))

sortAtmTime = sorted(atmTime)

for i in range(N):
    count += sortAtmTime[i] * (N - i)

print(count)