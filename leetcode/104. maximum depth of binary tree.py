from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, curnode, depth):
        if curnode.left == None and curnode.right == None:
            return depth
        
        left, right = depth, depth
        if curnode.left != None:
            left = self.dfs(curnode.left, depth+1)
        if curnode.right != None:
            right = self.dfs(curnode.right, depth+1)
        return max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left, right = 1, 1
        if root.left != None:
            left = self.dfs(root.left, 2)
        if root.right != None:
            right = self.dfs(root.right, 2)
        return max(left, right)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
        return dfs(root, 0)