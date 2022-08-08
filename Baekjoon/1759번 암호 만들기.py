# 입력
L, C = map(int, input().split())
# 주어지는 문자들 정렬
chrs = [c for c in input().split()]
chrs.sort()

# 가능한 단어들 담는 answer 리스트
answer = []

# 재귀 함수
def recur(i, word):
    # word 길이가 L이 되면 answer에 추가
    if len(word) == L:
        answer.append(word)
        return
    
    # 사전 순 정렬이므로 다음 인덱스부터 끝까지 탐색해서 한 글자씩 추가
    for idx in range(i+1, C):
        new_word = word + chrs[idx]
        recur(idx, new_word)

# 재귀 실행
for i in range(C-L+1):
    word = chrs[i]
    recur(i, word)

# answer에 있는 단어들 중 모음 최소 1개, 자음 최소 2개 이상인 것만 골라 출력
for word in answer:
	# 모음 vowel, 자음 conso
    vowel, conso = 0, 0
    # 모음, 자음 갯수 구하기
    for c in word:
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1
        else:
            conso += 1
    # 모음 1개 이상, 자음 2개 이상 출력
    if vowel >= 1 and conso >= 2:
        print(word)