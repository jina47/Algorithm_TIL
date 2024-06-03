from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sumNum = [sum(nums[:k])]
        for i in range(1, n-k+1):
            sumNum.append(sumNum[-1]-nums[i-1]+nums[i+k-1])
        maxNum = max(sumNum)
        return maxNum / k