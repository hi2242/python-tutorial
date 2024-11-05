import sys

input = sys.stdin.readline

def factorial(a):
    if(a == 0):
        return 1

    return a * factorial(a - 1)

# def combination(a, b):
#     return factorial(a) // (factorial(b) * factorial(a - b))

# def solve2(a):
#     result = 0

#     for i in range(a, -1, -2):
#         result += combination(a, i)
#         a -= 1

#     return result


factorialList = [1]

for i in range(1000):
    factorialList.append(factorialList[i] * (i + 1))



def solve(a):
    result = 0

    for i in range(a, -1, -2):
        result += (factorialList[a] // factorialList[i]) // factorialList[a - i]
        a -= 1

    return result

columnInput = int(input())

print(solve(columnInput) % 10007)
# print(solve2(columnInput) % 10007)