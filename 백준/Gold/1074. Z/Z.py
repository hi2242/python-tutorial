# row는 세로 인덱스 column은 가로 인덱스를 의미한다.
# 값을 변경하지 않으면 global 선언을 안해도 되고 변경할거면 global 선언을 해야한다.
# 4분할으로 재귀를 한다면 제 4사분면은 else로 정의한다.

# 재귀함수에서 return을 할 때는 재귀적으로 호출할 때 return을 붙여줘야 처음 실행되었던 함수까지
# 반환하고 싶은 값을 잘 가지고 오기 때문에 이 점을 유의해야 None이 출력되지 않는다.
import sys

input = sys.stdin.readline

N, row, column= map(int, input().split())

def solve(K, startX, startY, result):
    if K == 0:
        return

    K -= 1

    powK = 2 ** K
    powDoubleK = 4 ** K

    nx = startX + powK
    ny = startY + powK

    # 제 1사분면
    if row < ny and column >= nx:
        startX += 1 * powK
        startY += 0 * powK
        result += 1 * powDoubleK

    # 제 2사분면
    elif row < ny and column < nx:
        startX += 0 * powK
        startY += 0 * powK
        result += 0 * powDoubleK

    # 제 3사분면
    elif row >= ny and column < nx:
        startX += 0 * powK
        startY += 1 * powK
        result += 2 * powDoubleK

    # 제 4사분면
    else:
        startX += 1 * powK
        startY += 1 * powK
        result += 3 * powDoubleK

    if startY == row and startX == column:
        return result
    
    return solve(K, startX, startY, result)

answer = solve(N, 0, 0, 0)

print(answer)