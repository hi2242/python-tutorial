import sys

input = sys.stdin.readline

C = 0

for i in range(0, 100):
    A = str(input())
    if A.rstrip() == "":
        break   

    else:
        B = []
        for i in range (0, len(A)):
            if i < len(A) - 1:
                if A[i] != A[i + 1]:
                    B.append(A[i])
                    
                else:
                    continue
            else:
                break
        D = 0
        for i in range (0, len(B)):
            if D == 1:
                break
            elif ord(B[i]) < 97 or ord(B[i]) > 122:
                break
            elif len(B) == 1:
                C = C + 1
            for j in range (i + 1, len(B)):
                if B[i] == B[j]:
                    D = 1
                    break
                elif i == len(B) - 2:
                    C = C + 1
                else:
                    continue
                    

print(C)

# A = int(input())
# cnt = A

# for i in range(A):
#     word = input()
#     for j in range(len(word) - 1):
#         if word[j] == word[j+1]:
#             continue
#         elif word[j] in word[j+1:]:
#             cnt -= 1
#             break

# print(cnt)