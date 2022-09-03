N, M = map(int, input().split())
books = list(map(int, input().split()))

# 음수는 minus에, 양수는 plus에 담아줌
minus = []
plus = []
for book in books:
    if book < 0:
        minus.append(book)
    else:
        plus.append(book)
# 절댓값이 큰 순서대로 내림차순 정렬
minus.sort()
plus.sort(reverse=True)

# 인덱스 i가 M으로 나누어떨어지면 절댓값 answer에 담아줌
answer  = []
for i in range(len(minus)):
    if i % M == 0:
        answer.append(abs(minus[i]))
for i in range(len(plus)):
    if i % M == 0:
        answer.append(plus[i])
        
# answer의 합의 2배에서 최댓값 제거
print(sum(answer)*2-max(answer))