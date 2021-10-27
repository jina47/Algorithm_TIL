from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for k in course:
        combi = [i for j in orders for i in combinations(sorted(j), k)]
        count = Counter(combi)
    
        for c, i in count.items():
            if i == max(count.values()):
                if i >= 2:
                    answer.append(''.join(c))
    return sorted(answer)