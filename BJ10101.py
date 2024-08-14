import sys

input = sys.stdin.readline
a = []
for _ in range(3):
    a.append(int(input()))

a.sort()

if a[0] == a[1] == a[2] == 60:
    print("Equilateral")

elif sum(a) == 180:
    if a[0] == a[1] or a[1] == a[2]:
        print("Isosceles")

    else:
        print("Scalene")

else:
    print("Error")