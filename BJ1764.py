import sys

input = sys.stdin.readline

# set은 정수형 데이터인 경우에 한해서 자동 정렬까지 이루어지지만
# 문자형 데이터에서는 그렇지 않다. 그러므로 따로 sort를 해주어야한다.

N, M = map(int, input().split())

S = set()

for _ in range(N):
    S.add(input().rstrip())

result = S.copy()

for _ in range(M):
    S.discard(input().rstrip())

result -= S

sortResult = sorted(result)

print(len(sortResult))
print("\n".join(sortResult))