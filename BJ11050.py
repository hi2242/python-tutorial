import sys

input = sys.stdin.readline

def comPac(N, K):
    if K != 0:
        return N * comPac(N - 1, K - 1)
    else:
        return 1

N, K = map(int, input().split())

print(comPac(N, K) // comPac(K, K))

# pac = 1

# for i in range(K):
#     pac *= (N - i)
#     pac //= i + 1

# print(pac)