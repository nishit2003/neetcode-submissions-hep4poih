# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        res = root.val
        def dfs(node):
            if not node:
                return 0
            nonlocal res
            left = dfs(node.left)
            right = dfs(node.right)
            leftmax = max(left,0)
            rightmax = max(right,0)
        
            res = max(res, leftmax+rightmax+node.val)
            
            return node.val + max(leftmax,rightmax)
        
        dfs(root)
        return res