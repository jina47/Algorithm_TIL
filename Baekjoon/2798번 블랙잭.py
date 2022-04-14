import itertools
from itertools import combinations

N, M = map(int, input().split())
number = list(map(int, input().split()))

# M을 넘지 않게 number에서 3개를 뽑아 합을 return
num_com = []
for com in itertools.combinations(number, 3):
    if M < sum(com):
        continue
    else :
        num_com.append(sum(com))

print(max(num_com))