# 문제 규칙에 해당하는 입력 가능한 값을 리스트에 저장
rule = [3 * (2 ** i) for i in range(0, 11)]

n = int(input())

# 이차원 리스트 결과값 출력을 위한 함수 정의
def print_grid(array):
    for row in array:
        print("".join(row))

# 큰 삼각형 내부에 작은 삼각형 3개가 들어있는 형태로 Top-Down 구현을 하기 위한 파라미터
# 재귀적으로 호출하면서 Base Case를 지정하기 위한 파라미터 k를 n으로 초기값 설정
def solve(r, c, k = n):
    # Base case에 해당하는 부분으로 만약 k가 3이라면 별을 찍고 재귀를 멈춤
    # k는 해당 삼각형이 차지하는 크기 (3이 최소)
    if k == 3:
        # 형태에 맞게 삼각형 모양으로 별을 찍는다.
        star[r][c] = "*"
        for i in [-1, 1]:
            star[r + 1][c + i] = "*"
        for i in [-2, -1, 0, 1, 2]:
            star[r + 2][c + i] = "*"
        return

    # 삼각형이 차지하는 크기인 k를 절반으로 줄인 것을 t에 저장
    t = k // 2

    # 삼각형의 크기가 3보다 크다면 3개로 분할
    # r, c 좌표는 t를 이용하여 설정
    solve(r, c, t)
    solve(r + t, c - t, t)
    solve(r + t, c + t, t)

# 규칙에 알맞은 값인지 검증
if n in rule:
    # 별을 찍기 위해 미리 선언해둔 공백의 좌표 (세로는 n줄 가로는 2 * n 줄이어야 한다.)
    star = [[' ' for _ in range(2 * n)] for _ in range(n)]

    # 가장 처음엔 큰 삼각형의 상단 좌표부터 시작
    solve(0, n - 1, n)
    print_grid(star)