# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        isBalanced = True

        def height(root: Optional[TreeNode]) -> int:
            nonlocal isBalanced

            if not root:
                return 0
            height_left  = height(root.left) 
            height_right = height(root.right)

            if abs(height_left - height_right) > 1:
                isBalanced = False
            
            return 1 + max(height_left, height_right)
        height(root)
        return isBalanced