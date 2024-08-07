from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            left = 0
            right = len(matrix[0])-1
            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
    
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix:
#             return False
        
#         row = 0
#         col = len(matrix[0]) - 1

#         while row < len(matrix) and col >= 0:
#             if target == matrix[row][col]:
#                 return True
#             elif target < matrix[row][col]:
#                 col -= 1
#             else:
#                 row += 1

#         return False