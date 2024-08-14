import sys

input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())
fin = 0

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            fin = 1
            break

        else:
            continue

    if fin == 1:
        break


# if a == 0:
#     y = int(c / b)
#     x = int((f - e * y) / d)

# elif d == 0:
#     y = int(f / e)
#     x = int((c - b * y) / a)

# elif e - (b / a * d) != 0:    
#     y = int((f - (c / a * d)) / (e - (b / a * d)))
#     x = int((c - (b * y)) / a)

# print(x, y)