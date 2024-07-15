import sys

input = sys.stdin.readline
K = 0
A = []

for i in range(0, 100):
    S = str(input())
    if S.rstrip() == "" or S[0] == " " or S[len(S.rstrip())] == " ":
        break
    
    else:
        A.append(S)
        K = K + 1
    

for i in range(0, K):
    print(A[i].rstrip())

# import sys

# while True:
#   s = sys.stdin.readline().rstrip()
#   if s == '':
#     break
#   else:
#     print(s)