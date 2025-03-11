# DAC (분할 정복) 문항
# 지수 법칙 : A^(m + n) = A^m + A^n
# 나머지 분배 법칙
# 1. (A + B) % C = ((A % C) + (B % C)) % C
# 2. (A * B) % C = ((A % C) * (B % C)) % C
# 3. (A - B) % C = ((A % C) - (B % C) + C) % C

# 모듈러 연산 법칙
# 1. ((7^2 % 4) * (7^3 % 4)) % 4
# 2. ((7^2 % 4) * (7^2 % 4 * 7)) % 4
# 3. ((7^2 % 4) * (7 % 4 * 7 * 7)) % 4
# 4. ((1 % 4 * 7 * 7) * (1 % 4 * 7 * 7 * 7)) % 4 = 7^5 % 4
# 1, 2, 3, 4는 모두 같다.

import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

def solve(base, exp, div):
    if exp == 1:
        return base % div
    # asymtotic하게는 solve 재귀를 두번해도 똑같아 보이지만 실제 실행 시간에는 큰 영향이 있다.
    else:
        temp = solve(base, exp // 2, div)
        if exp % 2 == 1:
            return temp * (temp * base) % div
        else:
            return temp * temp % div
        
print(solve(A, B, C))