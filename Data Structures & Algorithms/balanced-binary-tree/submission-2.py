# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = 1 

        def height(root):
            nonlocal balanced
            if root is None:
                return 0
            
            r = height(root.right)
            l = height(root.left)

            if abs(r-l) > 1:
                balanced = 0
            
            return 1 + max(r, l)
        
        height(root)

        return balanced == 1
            