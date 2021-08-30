from itertools import combinations
def solution(nums):
    ls = list(combinations(nums, 3))
    answer = 0
    for i in ls:
        a = sum(i)
        n = 0 
        for j in range(2, int(sum(i)**0.5)+1):
            if a % j == 0:
                n += 1
                break
        if n == 0 and a >1:
            answer += 1

    return answer