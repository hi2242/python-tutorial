import sys

input = sys.stdin.readline

# [0] 기본 조건
# 중위 표기법 : 연산자가 피연산자 사이에 위치 ex. A + B
# 후위 표기법 : 연산자가 피연산자 뒤에 위치 ex. A B +

# [1] 중위 -> 후위 변환
# 1. 우선순위에 따라 괄호로 묶어준다.
# 2. 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨준다.
def solve():
    stack = []
    answer = []
    for i in exp:
        if i == "(":
            stack.append(i)

        elif i == ")":
            while stack:
                j = stack.pop()
                if j == "(":
                    break
                answer.append(j)

        elif i == "*" or i == "/":
            while stack:
                j = stack.pop()
                if j == "(" or j == "+" or j == "-":
                    stack.append(j)
                    break
                answer.append(j)
            stack.append(i)

        elif i == "+" or i == "-":
            while stack:
                j = stack.pop()
                if j == "(":
                    stack.append(j)
                    break
                answer.append(j)
            stack.append(i)

        else:
            answer.append(i)

    
    while stack:
        i = stack.pop()
        answer.append(i)

    return answer

# 입력
# 중위 표기식
# 단, 피연산자는 알파벳 대문자이고 한 번씩만 등장
# 단, 가장 앞에 -가 오거나 *가 생략되는 등의 수식은 주어지지 않음
# 단, 알파벳 대문자, +, -, *, /, (, )만 존재
# 단, 길이는 100을 넘지 않음
exp = list(input().rstrip())

# 출력
# 후위 표기식으로 바뀐 식 출력
print(*solve(), sep = "")
