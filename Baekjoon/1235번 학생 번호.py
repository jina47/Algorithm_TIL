N = int(input())
lst = []
for _ in range(N):
    lst.append(input()[::-1])


for i in range(len(lst[0])):
    temp = []
    for j in range(N):
        if int(lst[j][:i+1]) not in temp:
            temp.append(int(lst[j][:i+1]))
        else:
            break
    if len(temp) == N:
        print(i+1)
        break
