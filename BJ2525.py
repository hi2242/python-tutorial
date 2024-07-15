A, B = map(int, input().split())
C = int(input())

D = B + C

if D < 60:
    print(A, D)

else:
    if A + int(D / 60) < 24:
        print(A + int(D / 60), D % 60)

    else:
        print((A + int(D / 60)) % 24, D % 60)