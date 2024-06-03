str1 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"
str2 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"

if len(str1) < len(str2):
    temp = str1
    str1 = str2
    str2 = temp
print(len(str1), len(str2))
# str2 안에 반복 있는지 확인
t_list = []
i = 1
while i <= len(str2)//2+1:
    if i == len(str2)//2+1:
        t = str2
        t_list.append(t)
        break
    elif str2[0] == str2[len(str2)-i]:
        t = str2[len(str2)-i:]
        flag = True
        j = 0
        while j < len(str2):
            if str2[j:j+i] == t:
                j += i
                # print('here i, j:', i, j)
            else:
                flag = False
                break
        # print('here')
        if flag == True:
            t_list.append(t)
            i += 1
        else:
            i += 1
    else:
        i += 1

t_list = t_list[::-1]
print(t_list)

# t가 str1에서도 반복되는지 확인
for t in t_list:
    j = 0
    print('y', t, str1)
    flag = True
    while j < len(str1):
        if str1[j:j+len(t)] == t:
            j += len(t)
            print('here len, j:', len(str1), len(t), j)
        else:
            flag = False
            break
    if flag == True:
        print('real answer', t)
print('answer :', '')