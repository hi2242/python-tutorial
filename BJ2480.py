A, B, C = map(int, input().split())

if A == B == C:
    print(10000 + A * 1000)

elif A == B or A == C:
    print(1000 + A * 100)

elif B == C:
    print(1000 + B * 100)

else:
    if A > B and A > C:
        print(A * 100)

    elif B > A and B > C:
        print(B * 100)

    else:
        print(C * 100)

#가능할진 모르겠지만 elif 부분을 3개를 모두 묶은 후 sort한 후에 중간 값을 이용
#else의 부분을 max(a, b, c)를 이용하면 쉽게 해결된다.
