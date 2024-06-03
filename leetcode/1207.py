from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        check = {}
        for i, v in enumerate(arr):
            if v in check:
                check[v] += 1
            else:
                check[v] = 1
        isUnique = set(check.values())

        if len(isUnique) == len(check.keys()):
            return True
        else:
            return False