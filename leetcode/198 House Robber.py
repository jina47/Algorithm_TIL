from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        
        if len(nums) > 1:
            dp[1] = nums[1]
        else:
            return nums[0]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        
        return max(dp[-1], dp[-2])