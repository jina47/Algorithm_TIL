# 입력 문자열 T와 P
T = input()
P = input()

n = len(T)
m = len(P)

# P 내에 반복되는 문자열(패턴) 있는지 확인
def pattern(P, m):
    # lst는 접미어와 접두어가 같은 경우 가장 길이가 긴 길이를 담는 리스트
    # lst의 요소들은 어떤 인덱스로 돌아가서 값이 같은지 확인을 해야하는지를 알려주는 리스트
    lst = [0 for _ in range(m)]

    # i는 패턴의 위치를 가리키는 인덱스
    # j는 접미사의 위치를 가리키는 인덱스
    j = 0
    i = 1
    for i in range(1, m):
        # j가 0보다 크면 이전에 반복되는 패턴이 있었던 것
        # P[i] != P[j]이면 값이 같은지 확인해야하는 인덱스로 다시 j 지정
        while j > 0 and P[i] != P[j]:
            j = lst[j-1]

        # 만약 P[i] == P[j]라면 j += 1 해주고 lst[i] = j
        if P[i] == P[j]:
            j += 1
            lst[i] = j

        # j = 0인데 P[i]!=P[j]라면 lst[i] = 0

    # lst 리스트 return
    return lst

# P가 T에 있는지 확인
def KMP(P, T, n, m):
    lst = pattern(P, m)
    
    # j는 패턴의 인덱스
    j = 0
    # ans는 P가 나타나는 위치를 담는 리스트
    ans = []

    for i in range(n):
        # j > 0이고 T[i] != P[j]이면 겹치는 부분은 있으므로 j 위치를 이동
        while j > 0 and T[i] != P[j]:
            j = lst[j-1]
        
        # P[j] == T[i]라면 j 값이 m-1 미만이라면 j += 1
        # j가 m-1과 같으면 P가 T에 있는 것이므로 ans에 i+1-(m-1) = i-m+2 추가 
        if P[j] == T[i]:
            if j == m-1:
                ans.append(i-m+2)
                j = lst[j]
            else:
                j += 1
    
    # ans 리스트 return
    return ans


answer = KMP(P, T, n, m)
print(len(answer))
print(' '.join(map(str, answer)))