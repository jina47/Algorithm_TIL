# 입력 문자열 s
s = input()

# s의 길이
l = len(s)

happy, sad, i = 0, 0, 0

# 이모티콘 길이가 3이므로 i가 l-3 이하일 때까지 탐색
while i <= l-3:
    # :-) 는 happy,  :-( 는 sad
    # s[i] == ':' 이고 s[i+1] == '-'이면 i += 2 
    if s[i] == ':' and s[i+1] == '-':
        i += 2
        # s[i] 가 ')'이면 happy += 1 '('이면 sad += 1 그 후 i += 1
        if s[i] == ')':
            happy += 1
            i += 1
        elif s[i] == '(':
            sad += 1
            i += 1
    else:
        i += 1

# happy와 sad의 개수를 비교해서 값 출력
if happy == 0 and sad == 0:
    print('none')
elif happy == sad:
    print('unsure')
elif happy > sad:
    print('happy')
elif sad > happy:
    print('sad')



