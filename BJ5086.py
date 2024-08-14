import sys

input = sys.stdin.readline

p = []

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    else:
        if B % A == 0:
            p.append("factor")

        elif A % B == 0:
            p.append("multiple")

        else:
            p.append("neither")
        continue

print(*p, sep = "\n")