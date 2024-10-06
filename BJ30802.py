import sys

input = sys.stdin.readline

N = int(input())

shirt = list(map(int, input().split()))

T, P = map(int, input().split())

count = 0

for i in range(6):
    if shirt[i] % T == 0:
        count += (shirt[i] // T)
    
    else:
        count += (shirt[i] // T) + 1

print(count)
print((N // P), (N % P))