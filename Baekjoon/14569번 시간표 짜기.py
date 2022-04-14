N = int(input())
subject = []
for _ in range(N):
    ipt = input().split()
    subject.append(ipt[1:])
M = int(input())
for _ in range(M):
    timetable = input().split()[1:]
    possible = 0
    for sub in subject:
        if len(set(sub)- set(timetable)) == 0:
            possible += 1
    print(possible)