string = input()
# string의 알파벳과 string에서의 인덱스를 담는 lst
lst = []
for i, s in enumerate(string):
    lst.append([s, i])
lst.sort()
print(lst)

# lst[0][0]이 사전순으로 가장 빠른 알파벳 출력
alpha, start = lst[0]
answer = ['' for _ in range(len(string))]
answer[start] = alpha
end = start
print(alpha)

# end보다 더 크고 (string에서 뒷쪽에 위치) 아직 쓰지 않은 단어라면 출력, start와 end 갱신
for i in range(1, len(lst)):
    if lst[i][1] > end and answer[lst[i][1]] == '':
        start = end
        end = lst[i][1]
        answer[end] = lst[i][0]
        print(''.join(answer))

# end가 -1이 되면 break하는 while 반복문
while end > -1:
    # lst를 탐색하면서 start와 end 사이 인덱스에 해당하는 알파벳이라면 answer에 넣어 출력, start 갱신
    if end - start > 1:
        for i in range(1, len(lst)):
            if start < lst[i][1] < end and answer[lst[i][1]] == '':
                answer[lst[i][1]] = lst[i][0]
                print(''.join(answer))
                start = lst[i][1]
    
    # start와 end 차이가 1이면 start와 end 다시 정하기
    end = start
    for a in range(end-1, -1, -1):
        if answer[a] != '':
            start = a
            break
    else:
        start = -1

