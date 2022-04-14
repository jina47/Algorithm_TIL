N = int(input())
temp = []
# 나중에 원래 들어왔던 순서대로 출력하기 위해 index도 함께 배열에 넣어줌
for idx in range(2*N-2):
    temp.append([input().strip(), idx])

# temp를 문자열 길이 순서대로 정렬
temp = sorted(temp, key=lambda x: (len(x[0]), x[1]))

# 문자열 S 구하기
# 가장 긴 길이를 가지는 문자열 2개로 S의 조합을 만들어 보고 S의 첫 글자와 끝 글자가 맞는지 확인
if temp[-1][0] + temp[-2][0][-1] == temp[-1][0][0] + temp[-2][0]:
    S = temp[-1][0] + temp[-2][0][-1]
    if (S[0] == temp[0][0] and S[-1] == temp[1][0]) or (S[0] == temp[1][0] and S[-1] == temp[0][0]):
        pass
    else:
        S = temp[-2][0] + temp[-1][0][-1]
else:
    S = temp[-2][0] + temp[-1][0][-1]
print(S)

# 접두사인지 접미사인지 판별
for i in range(0, 2*N-2, 2):
    if S[:len(temp[i][0])] == temp[i][0] and S[N-len(temp[i][0]) == temp[i+1][0]:]:
        temp[i].append('P')
        temp[i+1].append('S')
    else:
        temp[i].append('S')
        temp[i+1].append('P')

# 원래 들어왔던 문자열 순서대로 접두사, 접미사 출력
temp.sort(key=lambda x: x[1])
print(''.join(s[2] for s in temp))