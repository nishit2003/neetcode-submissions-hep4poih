# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root:
                return 0

            l_height = height(root.left)
            if l_height == -1:
                return -1

            r_height = height(root.right)
            if r_height == -1:
                return -1

            if abs(l_height - r_height) > 1:
                return -1
            
            return 1 + max(l_height, r_height)


        return height(root) != -1