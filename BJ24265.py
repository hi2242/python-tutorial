import sys

input = sys.stdin.readline

n = int(input())

if n % 2 != 0:
    print(n * (n // 2))

else:
    print((n * (n - 1) // 2))

print(2)