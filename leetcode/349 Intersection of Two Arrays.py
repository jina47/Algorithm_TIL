from typing import List
import bisect


# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         if len(nums1) > len(nums2):
#             nums1, nums2 = nums2, nums1
#         nums1.sort()
#         nums2.sort()

#         # nums1가 더 작은 쪽이니 nums2를 binary search
#         target = nums1[0]
#         left = 0
#         right = len(nums2) - 1
#         j = -1
#         while left < right:
#             mid = (left + right) // 2
#             if nums2[mid] == target:
#                 j = mid
#                 break
#             elif nums2[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         if  j == -1:
#             j = left

#         result = []
#         i = 0
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] == nums2[j]:
#                 if result and result[-1] != nums1[i]:
#                     result.append(nums1[i])
#                 elif not result:
#                     result.append(nums1[i])
#                 i += 1
#                 j += 1
#             elif nums1[i] < nums2[j]:
#                 i += 1
#             else:
#                 j += 1
        
#         return result
    

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if result and result[-1] != nums1[i]:
                    result.append(nums1[i])
                elif not result:
                    result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return result
    

# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         result = set()
#         nums2.sort()
#         for n1 in nums1:
#             i2 = bisect.bisect_left(nums2, n1)
#             if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
#                 result.add(n1)
#         return result


# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums1.sort()
#         nums2.sort()
#         result = set()
#         i = 0
#         j = 0
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] == nums2[j] and nums1[i] not in result:
#                 result.add(nums1[i])
#                 i += 1
#                 j += 1
#             elif nums1[i] < nums2[j]:
#                 i += 1
#             else:
#                 j += 1
        
#         return result