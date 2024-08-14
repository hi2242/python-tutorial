import sys

input = sys.stdin.readline


T = int(input())

result = [[0] * 4 for _ in range(T)]

for i in range(T):
    C = int(input())
    for _ in range(4):
        if 25 <= C:
            result[i][0] = int(C / 25)
            C -= result[i][0] * 25
        
        elif 10 <= C:
            result[i][1] = int(C / 10)
            C -= result[i][1] * 10

        elif 5 <= C:
            result[i][2] = int(C / 5)
            C -= result[i][2] * 5

        else:
            result[i][3] = int(C / 1)
    
for row in result:
    print(' '.join(map(str, row)))

# for row in range(T):
    # print(*result[row], end = "\n")