import sys

input = sys.stdin.readline

A, B, V = map(int, input().split())

D = 0

D = ((V - A) / (A - B)) + 1

if (V - A) % (A - B) != 0:
    D += 1

print(int(D))