N = int(input())
switch = [0] + list(map(int, input().split()))
S = int(input())
student = []
for _ in range(S):
    student.append(list(map(int, input().split())))

for [sex, number] in student:
    # 남자인 경우
    if sex == 1:
        for j in range(1, N+1):
            if j % number == 0:
                if switch[j] == 0:
                    switch[j] = 1
                else:
                    switch[j] = 0
    # 여자인 경우
    else:
        cnt = 0
        while True:
            left = number-cnt
            right = number+cnt
            if 0 < left and right < N+1 and switch[left] == switch[right]:
                if switch[left] == 0:
                    switch[left] = 1
                else:
                    switch[left] = 0
                if left != right:
                    if switch[right] == 0:
                        switch[right] = 1
                    else:
                        switch[right] = 0
            else:
                break
            cnt += 1

                
for i in range(1, len(switch)):
    if i != 1 and i % 20 == 1:
        print()
    print(switch[i], end=' ')

