import sys

input = sys.stdin.readline

n = int(input())

if n >= 3:
    print((n * (n - 1) * (n - 2)) // (3 * 2 * 1))
else:
    print(0)

print(3)