# 입력값 N
N = int(input())

# S의 길이 M
M = int(input())

# 문자열 S
S = input()

# Pn은  'I' + 'OI' * N, 'IOI'가 N개 반복되는 패턴으로 이루어짐
Pn = 'IO' * N + 'I'

# S에 Pn이 몇 개 존재하는지 확인
# cnt로 조건을 만족하는 경우의 수(ans) 구하기
ans = 0
cnt = 0
i = 0
while i < M-2:
    # S[i:i+3]이 'IOI'인 경우 cnt += 1
    if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I':
        cnt += 1
        # cnt가 N을 만족하면 ans+=1, cnt-=1
        if cnt == N:
            ans += 1
            cnt -= 1
        # IOI가 있을 때는 다음 I를 확인해주면 되므로 i += 2
        i += 2

    # S[i:i+3]이 'IOI'가 아닌 경우 cnt = 0
    else:
        cnt = 0
        # S[i+1]을 확인하기 위해 i += 1
        i += 1

# ans 출력
print(ans)


## 새로 다시 풀어본 풀이

# P의 길이 N, S의 길이 M, 문자열 S
N = int(input())
M = int(input())
S = input()

# S의 인덱스 i, IOI개수 카운트 cnt, P의 개수 answer
i = 0
cnt = 0
answer = 0

# 인덱스 탐색 (S의 끝에서 세번째까지만 탐색하면 됨)
while i < M-2:
    # 'IOI'인 경우 cnt += 1 해주고 그 다음 문자도 'IOI'인지 탐색하기 위해 i += 2
    if S[i] + S[i+1] + S[i+2] == 'IOI':
        cnt += 1
        i += 2
    # 'IOI'아닌 경우 cnt 초기화, 그 다음 인덱스 탐색을 위해 i += 1
    else:
        cnt = 0
        i += 1
    
    # 만약 cnt == N이라면 P가 하나 들어있는 것이므로 answer += 1, 그 다음 탐색을 위해 cnt -= 1    
    if cnt == N:
        answer += 1
        cnt -= 1

# 정답 출력    
print(answer)