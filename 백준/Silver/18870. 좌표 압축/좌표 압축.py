# 시간복잡도 측면에서 dictionary가 제일 좋다.
# hash mapping 하듯 :로 dictionary를 정의하면 된다.
import sys

input = sys.stdin.readline

count = int(input())

beforePoints = list(map(int, input().split()))

setPoints = set(beforePoints)

sortedPoints = sorted(setPoints)

dictionaryPoints = {sortedPoints[i] : i for i in range(len(setPoints))}

for eachPoint in beforePoints:
    print(dictionaryPoints[eachPoint], end = " ")