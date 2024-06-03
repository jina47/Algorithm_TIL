from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, curnode, path, answer):
        if curnode.left == None and curnode.right == None:
            answer.append(path[:-2])
            return 

        for child in range(2):
            if child == 0 and curnode.left != None:
                self.dfs(curnode.left, path+str(curnode.left.val)+"->", answer)
            elif child == 1 and curnode.right != None:
                self.dfs(curnode.right, path+str(curnode.right.val)+"->", answer)


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        self.dfs(root, str(root.val)+"->", answer)

        return answer
    