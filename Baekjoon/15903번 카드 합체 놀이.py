import sys
from heapq import heappush, heappop

n, m = map(int, sys.stdin.readline().strip().split())
cards = list(map(int, sys.stdin.readline().strip().split()))
cards.sort()

for i in range(m):
    # cards의 가장 작은 두 개 꺼내서 더해준 후 다시 cards에 넣어줌
    x = heappop(cards)
    y = heappop(cards)
    heappush(cards, x+y)
    heappush(cards, x+y)

# cards의 합 출력    
print(sum(cards))
