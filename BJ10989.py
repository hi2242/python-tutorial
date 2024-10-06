import sys

input = sys.stdin.readline

# 계수 정렬 (입력받는 수가 제한범위가 정해져있을 때)
# 10000칸의 표를 만들어서 입력에 해당하는 인덱스를 1씩 카운트한다.
# 최종적으로 인덱스에 해당하는 카운트 수만큼 인덱스를 출력한다.
N = int(input())

arr = [0] * 10000

for _ in range(N):
    arr[int(input()) - 1] += 1

for i in range(10000):
    if N == 0:
        break
    for _ in range(arr[i]):
        print(i + 1)
        N -= 1