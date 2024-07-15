# <문제>
# n개의 정수가 주어질때 다음 두 조건을 만족하는 함수
# 1. 원소를 n으로 나눈 나머지와 인덱스 번호가 같도록 최대한 배치한다.
# 2. 배치된 경우의 수중 앞에 있는 숫자가 더 작은 배열을 선택한다.
# <예시>
# 2 5 6 13 14 16 35 -> 14 2 16 6 35 5 13
# 11 12 31 21 16 25 77 48 88 45 -> 11 21 12 25 31 45 16 77 48 88

import sys

input = sys.stdin.readline

def ASD (n, vals):
    answer = []
    B = 0
    C = []
    D = []

    for i in range(0, n):
        answer.append(vals[i] % n)

    # for i in range(0, n):
    #     for j in range(0, n):
    #         if answer[j] == i:
    #             B = answer[j]
    #             answer[j] = answer[i]
    #             answer[i] = B
    #             B = vals[j]
    #             vals[j] = vals[i]
    #             vals[i] = B
    #         else:
    #             continue
 
    for i in range(0, n):
        for j in range(0, n):
            if answer[j] == i:
                B = answer[j]
                answer[j] = answer[i]
                answer[i] = B
                B = vals[j]
                vals[j] = vals[i]
                vals[i] = B



            else:
                continue

    for i in range(0, n):
        for j in range(0, n):
            if answer[i] == answer[j] and vals[j] > vals[i]:
                B = answer[j]
                answer[j] = answer[i]
                answer[i] = B
                B = vals[j]
                vals[j] = vals[i]
                vals[i] = B

            else:
                continue

    for i in range(0, n):
        if i != answer[i]:
            C.append(vals[i])
            C.sort()
            D.append(i)

        else:
            continue

    for i in range(0, len(C)):
        vals[D[i]] = C[i]
    # for i in range(0 , n):
    #     for j in range(0, n):
    #         if answer[j] != i:
    #             vals[j] = C[i]
    #         else:
    #             continue
            
    return vals, C
print(ASD(7, [2, 5, 6, 13, 14, 16, 35]))
print(ASD(10, [11, 12, 31, 21, 16, 25, 77, 48, 88, 45]))