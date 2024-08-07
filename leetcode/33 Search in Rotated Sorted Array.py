from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
    


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if not nums:
#             return -1
        
#         left = 0
#         right = len(nums) - 1
        
#         while left < right:
#             mid = (left + right) // 2

#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid

#         pivot = left

#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             mid_pivot = (mid + pivot) % len(nums)

#             if nums[mid_pivot] < target:
#                 left = mid + 1
#             elif nums[mid_pivot] > target:
#                 right = mid - 1
#             else:
#                 return mid_pivot
        
#         return -1