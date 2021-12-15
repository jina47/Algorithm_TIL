def find_next(id, alphabet, answer):
    # id가 0이 될 떄까지 while문 반복
    while id >= 1:
        # id보다 하나 작은 값이 인덱스와 같은 알파벳을 아스키 코드로 변환
        ix = ord(answer[id-1])-97
        # alphabet[ix] 는 0으로 바꿔줌
        alphabet[ix] = 0
        
        # ix+1의 값부터 26의 값까지 탐색하면서 alphabet의 값이 0이 되면 현재 answer값의 끝 값을 chr(j+97)로 바꿔서 저장 후 출력, 함수 빠져나옴
        for j in range(ix+1, 26):
            if alphabet[j] == 0:
                answer = answer[:id-1] + chr(j+97)
                print(answer)
                return
        # 아직 쓰지 않은 알파벳이 없으면 id에서 1을 뺴주고 같은 과정 반복
        else:
            id -= 1
    # 과정을 다 돌았는데도 다음 단어를 찾지 못했다면 -1 출력
    print(-1)
    return

# 입력 S에 들어있는 알파벳은 1로 표시
alphabet = [0 for _ in range(26)]
S = input()
for s in S:
    idx = ord(s)-97
    alphabet[idx] = 1

answer = S
# S의 길이가 26보다 작으면 모든 알파벳을 다 사용한 것이 아니므로 맨 끝에 아직 사용하지 않은 알파벳 중 가장 앞 글자를 더해 출력
if len(S) < 26:    
    for i in range(26):
        if alphabet[i] == 0:
            answer += chr(i+97)
            print(answer)
            break
# 만약 S의 길이가 26이라면 가장 끝 값의 알파벳은 0으로 바꿔주고 다음 다양한 단어를 찾는 함수 실행
else:
    alphabet[ord(answer[25])-97] = 0
    find_next(25, alphabet, answer)
