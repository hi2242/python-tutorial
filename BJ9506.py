import sys

input = sys.stdin.readline

while True:
    n = int(input())
    A = []
    if n == -1:
        break

    else:
        for i in range(n - 1):
            if n % (i + 1) == 0:
                A.append(i + 1)

            else:
                continue

        if n == sum(A):
            print(n, end = " = ")
            print(*A, sep = " + ")

        else:
            print(n, "is NOT perfect.")