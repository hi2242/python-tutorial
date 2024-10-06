import sys

input = sys.stdin.readline

result = []

while True:
    length = list(map(int, input().split()))
    if (length == [0, 0, 0]):
        break
    else:
        length.sort()
        if ((length[0] ** 2) + (length[1] ** 2) == (length[2] ** 2)):
            result.append("right")

        else:
            result.append("wrong")

for A in result:
    print("".join(map(str, A)))