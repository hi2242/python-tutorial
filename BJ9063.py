import sys

input = sys.stdin.readline

N = int(input())
x = []
y = []

for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

if N >= 2:
    print((x[0] - x[N - 1]) * (y[0] - y[N - 1]))

else:
    print(0)