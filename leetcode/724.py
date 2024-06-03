from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums) - nums[0]
        if left == right:
            return 0
        
        for pivot in range(1, len(nums)):
            left += nums[pivot-1]
            right -= nums[pivot]
            if left == right:
                return pivot

        return -1