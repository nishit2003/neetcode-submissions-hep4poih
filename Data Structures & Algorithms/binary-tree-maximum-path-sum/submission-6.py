# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = -float('inf')

        def dfs(node):
            if not node:
                return 0
            nonlocal res
            left = dfs(node.left)
            right = dfs(node.right)
            leftMax = max(0,left)
            rightMax = max(0,right)

            res = max(res,leftMax + rightMax + node.val)
            return node.val + max(leftMax,rightMax)
        
        dfs(root)
        return res