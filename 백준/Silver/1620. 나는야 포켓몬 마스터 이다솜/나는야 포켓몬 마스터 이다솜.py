import sys

input = sys.stdin.readline

# rstrip를 통해 입력 뒤에 붙는 공백을 지울 수 있다.
# in을 통해 list에 있는 요소를 확인할 수 있다.
# 시간복잡도가 더 나은 dictionary를 사용하여 양방향으로 찾을 수 있게 인덱스와 이름의 양쪽 해쉬맵을 만든다.
# isdigit은 문자열이 숫자로만 이루어졌으면 True 하나라도 문자가 껴있으면 False를 반환한다.
pocketMonster = {}
answer = []
monsterCount, questionCount = map(int, input().split())

for i in range(monsterCount):
    monsterName = input().rstrip()
    pocketMonster[i + 1] = monsterName
    pocketMonster[monsterName] = i + 1

for _ in range(questionCount):
    question = input().rstrip()
    if question.isdigit():
        answer.append(pocketMonster[int(question)])

    else:
        answer.append(pocketMonster[question])

for ans in answer:
    print(ans)