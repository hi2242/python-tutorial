import sys

input = sys.stdin.readline

acc = float(0.0)
average = 0
total = float(0.0)

for i in range(20):
    subject = list(map(str, input().split()))
    acc += float(subject[1])
    # subjectInfo = []
    # subject = input().split()
    # subjectInfo.append(subject)
    # print(subjectInfo[0][1])
    if subject[2] == "A+":
        total += float(subject[1]) * 4.5
    elif subject[2] == "A0":
        total += float(subject[1]) * 4.0
    elif subject[2] == "B+":
        total += float(subject[1]) * 3.5
    elif subject[2] == "B0":
        total += float(subject[1]) * 3.0
    elif subject[2] == "C+":
        total += float(subject[1]) * 2.5
    elif subject[2] == "C0":
        total += float(subject[1]) * 2.0
    elif subject[2] == "D+":
        total += float(subject[1]) * 1.5
    elif subject[2] == "D0":
        total += float(subject[1]) * 1.0
    elif subject[2] == "F":
        total += float(subject[1]) * 0.0
    else:
        acc -= float(subject[1])
        continue

average = total / acc

print(average)
