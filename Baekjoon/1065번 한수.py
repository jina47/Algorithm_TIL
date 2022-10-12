N = int(input())

# 100 이하 수는 모두 등차수열 만족
if N < 100:
    print(N)
# 100 이상의 수는 등차수열 만족하는지 확인
else:
    cnt = 99
    for num in range(100, N+1):
        word = str(num)
        gap = int(word[0]) - int(word[1])
        # gap이 다른 구간이 있다면 등차수열 만족하지 못함
        for i in range(1, len(word)-1):
            if int(word[i]) - int(word[i+1]) != gap:
                break
        # break되지 않으면 등차수열 만족하므로 cnt += 1
        else:
            cnt += 1
    # cnt 출력
    print(cnt)
