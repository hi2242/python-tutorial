import sys

input = sys.stdin.readline

C = []
i = int(0)
while True:
    try :
        A, B = map(int, input().split())
        i = i + 1
        C.append(A + B)
    except:
         break

for j in range(0, i):
    print(C[j])