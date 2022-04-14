# 테스트케이스
T = int(input())

for _ in range(T):
    # 입력값
    S = input()

    # 공백 기준으로 단어 나누기
    S_lst = S.split()
    
    answer = ''
    for i, word in enumerate(S_lst):
        answer += word[::-1]
        if i != len(S_lst)-1:
            answer += ' '
    
    # 출력        
    print(answer)