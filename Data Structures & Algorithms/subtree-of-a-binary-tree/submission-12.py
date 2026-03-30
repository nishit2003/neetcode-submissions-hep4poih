# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        # if not subRoot and root:
        #     return True
        
        return self.sametree(root, subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def sametree(self,p,q):
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return self.sametree(p.left,q.left) and self.sametree(p.right,q.right)