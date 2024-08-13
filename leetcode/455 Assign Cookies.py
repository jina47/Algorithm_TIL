from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for j in range(len(s)):
            if i >= len(g):
                break
            elif s[j] >= g[i]:
                i += 1
        
        return i
    

# class Solution:
#     def findContentChildren(self, g: List[int], s: List[int]) -> int:
#         g.sort()
#         s.sort()

#         i, j = 0, 0
#         while i < len(g) and j < len(s):
#             if s[j] >= g[i]:
#                 i += 1
#             j += 1
        
#         return i