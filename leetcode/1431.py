from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        max_candy = max(candies)
        for kid in range(len(candies)):
            if candies[kid] + extraCandies >= max_candy:
                answer.append(True)
            else:
                answer.append(False)
        return answer