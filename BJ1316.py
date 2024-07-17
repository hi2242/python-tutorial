import sys

input = sys.stdin.readline

A = input().split()

if A
    print(A, D)

else:
    if A + int(D / 60) < 24:
        print(A + int(D / 60), D % 60)

    else:
        print((A + int(D / 60)) % 24, D % 60)