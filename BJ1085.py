import sys

input = sys.stdin.readline

x, y, w, h = map(int, input().split())

a, b = 0, 0

if x >= y:
    a = y
else:
    a = x

if w - x >= h - y:
    b = h - y
else:
    b = w - x

if a >= b:
    print(b)

else:
    print(a)