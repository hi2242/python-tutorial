import sys

input = sys.stdin.readline

PRIM_NUM = 1000000007

# [0] 기본 정보
# 피보나치 수 : 0 1 1 2 3 5 8 13 21 34 55 ...
# Fn = Fn-1 + Fn-2 (n >= 2)
# n이 주어졌을 때 n번째 피보나치 수 구하기

# [1] 피보나치
# (0, 1) : Fn-3개만큼 있음
# (1, 1) : Fn-2개만큼 있음
def multi_array(array_A, array_B):
    return [[(array_A[0][0] * array_B[0][0] + array_A[0][1] * array_B[1][0]) % PRIM_NUM,
             (array_A[0][0] * array_B[0][1] + array_A[0][1] * array_B[1][1]) % PRIM_NUM],
             [(array_A[1][0] * array_B[0][0] + array_A[1][1] * array_B[1][0]) % PRIM_NUM,
              (array_A[1][0] * array_B[0][1] + array_A[1][1] * array_B[1][1]) % PRIM_NUM]]

def calc_order(k):
    calc = []
    while k != 1:
        if k % 2 == 1:
            k -= 1
            calc.append("multi")

        else:
            k //= 2
            calc.append("power")

    return calc

def solve(k):
    array = [[1, 1], [1, 0]]
    curr = [[1, 1], [1, 0]]
    calc = calc_order(k)

    for i in calc[::-1]:
        if i == "multi":
            curr = multi_array(curr, array)

        else:
            curr = multi_array(curr, curr)
    
    return curr[0][1]

# 입력
# n
# 단, n <= 1000000000000000000인 자연수
n = int(input())

# 출력
# n번째 피보나치 수를 1000000007로 나눈 나머지 출력
print(solve(n) % PRIM_NUM)