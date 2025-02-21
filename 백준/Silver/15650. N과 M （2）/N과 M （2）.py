# combination 조합에 대한 문제로 재귀를 통해 해결해야 한다.
# result.append(arr[i])를 사용하게 되면 원본 리스트를 직접 수정하여
# 재귀 호출될 때 result가 공유되므로 의도대로 작동하지 않는다.
# 재귀 호출 시 start를 i + 1로 설정하는 이유는 뒤집어서 중복이 되는 조합을
# 제외하기 위함이다.
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

testCase = []

def solve(arr, n, start = 0, result = []):
    if n > len(arr):
        return
    
    if len(result) == n:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, len(arr)):
        solve(arr, n, i + 1, result + [arr[i]])

for i in range(N):
    testCase.append(i + 1)

solve(testCase, M)
