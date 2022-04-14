# 입력
N = int(input())
time = []
for _ in range(N):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x: (x[0], x[1]-x[0]))


answer = []
for i, t in enumerate(time):
    if i == 0:
        answer.append(t)
        temp = t
    else:
        if t[0] < temp[1]:
            if t[1] < temp[1]:
                temp = t
                answer.pop()
                answer.append(temp)
        else:
            answer.append(t)
            temp = t
print(len(answer))
        


            


