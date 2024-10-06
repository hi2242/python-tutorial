import sys

input = sys.stdin.readline

result = []

while True:
    testCase = list(map(int, input().rstrip()))
    if testCase == [0]:
        break
    else:
        rTestCase = list(reversed(testCase))
        # reverse()는 리턴 값이 None이므로 역순을 리턴하려면 list(reversed())를 사용한다.
        if testCase == rTestCase:
            result.append("yes")
        
        else:
            result.append("no")

for X in result:
    print(''.join(map(str, X)))