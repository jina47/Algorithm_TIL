from typing import List
import bisect


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left = i + 1
            right = len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[i] + numbers[mid] == target:
                    return [i+1, mid+1]
                elif numbers[i] + numbers[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         i = 0
#         j = len(numbers)-1
#         while i < j:
#             if numbers[i] + numbers[j] == target:
#                 return [i+1, j+1]
#             elif numbers[i] + numbers[j] < target:
#                 i += 1
#             elif numbers[i] + numbers[j] > target:
#                 j -= 1
                

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for k ,v in enumerate(numbers):
#             expected = target - v
#             i = bisect.bisect_left(numbers, expected, k+1)
#             if i < len(numbers) and numbers[i] == expected:
#                 return k+1, i+1