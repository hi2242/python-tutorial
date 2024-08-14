import sys

input = sys.stdin.readline

a = list(map(int, input().split()))
b = 0
a.sort()

if a[2] >= a[0] + a[1]:
    b = 2 * (a[0] + a[1]) - 1
    print(b)

else:
    print(sum(a))