import sys

input = sys.stdin.readline

a1, a0 = map(int, input().split())

c = int(input())

n0 = int(input())

n = n0


if c >= a1 and (a1 * n + a0) <= c * n:
    print(1)

else:
    print(0)