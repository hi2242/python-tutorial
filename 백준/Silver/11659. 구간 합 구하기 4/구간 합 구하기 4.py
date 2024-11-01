# list를 index로 slice하려면 list명[시작 인덱스 : slice할 개수 : step]을 이용한다.
# 시간복잡도를 고려하여 DP로 누적 합을 미리 저장하고 그 차를 이용하여 구간 합을 구하는 문제이다.
import sys

input = sys.stdin.readline

inputN, countM = map(int, input().split())

numberList = list(map(int, input().split()))

sumList = [0]
accumulate = 0
for i in range(inputN):
    accumulate += numberList[i]
    sumList.append(accumulate)

for i in range(countM):
    start, end = map(int, input().split())
    result = 0
    result = sumList[end] - sumList[start - 1]
    print(result)