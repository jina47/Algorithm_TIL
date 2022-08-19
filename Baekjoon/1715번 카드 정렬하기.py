from heapq import heappush, heappop

# 입력
N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))
cards.sort()

# heapq 이용하기 (최소 힙)
answer = 0
while len(cards) > 1:
    # cards에서 가장 작은 수 2개 뽑아서 더해주기
    small = heappop(cards) + heappop(cards)
    # answer에 더해주기
    answer += small
    # cards에 small 다시 넣어주기
    heappush(cards, small)

# 출력

print(answer)

# while len(cards) > 1:
#     cards.sort()
#     small = cards.pop(0)
#     answer += cards[0] + small
#     cards[0] += small
#     print(cards)
# print(answer)