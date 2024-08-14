import sys

input = sys.stdin.readline

while True:
    a = []
    a = list(map(int, input().split()))
    a.sort()

    if a[0] == a[1] == a[2] == 0:
        break

    elif a[0] + a[1] <= a[2]:
        print("Invalid")

    elif a[0] == a[1] == a[2]:
        print("Equilateral")

    elif a[0] == a[1] or a[1] == a[2]:
        print("Isosceles")

    elif a[0] != a[1] != a[2]:
        print("Scalene")