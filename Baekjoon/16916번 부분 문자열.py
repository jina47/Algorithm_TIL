# 입력 문자열 T와 P
S = input()
P = input()

n = len(S)
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

# P가 S에 있는지 확인
def KMP(P, S, n, m):
    lst = pattern(P, m)
    
    # j는 패턴의 인덱스
    j = 0

    #ans는 P가 S에 있으면 1 없으면 0
    ans = 0

    for i in range(n):
        # j > 0이고 S[i] != P[j]이면 겹치는부분은 있으므로 j 위치를 이동
        while j > 0 and S[i] != P[j]:
            j = lst[j-1]
        
        # P[j] == S[i]라면 j 값이 m-1 미만이라면 j += 1
        # j가 m-1과 같으면 P가 S에 있는 것이므로 ans = 1이고 return ans 
        if P[j] == S[i]:
            if j == m-1:
                ans = 1
                return ans
            else:
                j += 1
    # ans가 0이면 P가 S에 없는 것이므로 0 return
    return ans


answer = KMP(P, S, n, m)
print(answer)




# ## 보이어 무어 알고리즘
# ## 오른쪽 끝부터 왼쪽으로 비교
# ## 뒤에서부터 비교하다가 다른 부분이 나오면 일치하는 문자가 있는 곳까지 이동
# ## 일치하는 부분이 하나도 없다면 찾는 문자열의 길이만큼 이동

# def findidx(P, temp, j, m):
#     for idx in range(j-1, -1, -1):
#         if P[idx] == temp:
#             return idx
#     return j-m

# i = 0
# j = m-1
# while j >= 0 and i <= n-m:

#     if P[j] == S[i+j]:
#         j -= 1
#     else:
#         shift = findidx(P, S[i+j], j, m)
#         i += j-shift
#         j = m-1

#     if j == -1:
#         print(1)
#         break

# if j != -1:
#     print(0)

