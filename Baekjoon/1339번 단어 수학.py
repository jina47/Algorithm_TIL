# 입력
N = int(input())
# 각 알파벳마다 더해지는 숫자를 담아주는 리스트 alpha
alpha = [0 for _ in range(26)]
for _ in range(N):
    word = input()
    for i, a in enumerate(word):
        alpha[ord(a)-65] += 10**(len(word)-i-1)
print(alpha)
# 내림차순 정렬
alpha.sort(reverse=True)

# N개 단어의 최대 합 구하기
answer = 0
num = 9
for b in alpha:
    if b == 0:
        break
    # answer에 더해주기
    answer += b * num
    # 알파벳에 숫자 배정해주었으면 다음 숫자는 -1 해줘야 함
    num -= 1

# 출력
print(answer)


