import sys

input = sys.stdin.readline

# lambda 매개변수 : 표현식

# def hap(x, y):
#      return x + y
# hap(10, 20) ===> 결과 : 30

# (lambda x, y: x + y)(10, 20) ===> 결과 : 30

N = int(input())
stringList = []
stringList.append(input().rstrip())

for i in range(N - 1):
    word = input().rstrip()
    stringList.append(word)

sortStringList = sorted(stringList, key = lambda x : (len(x), x))
# len(x)는 원소의 길이 별로 분류 한 후에 x는 그냥 기존 sorted를 적용한 것이다.

count = 1
while count != len(sortStringList):
    if sortStringList[count] == sortStringList[count - 1]:
        sortStringList.pop(count)
        count = 1
    else:
        count += 1

print("\n".join(sortStringList))