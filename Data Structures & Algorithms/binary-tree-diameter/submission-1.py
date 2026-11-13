# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(root):
            nonlocal diameter

            if root is None:
                return 0
            
            r = height(root.right)
            l = height(root.left)

            diameter = max(diameter, r + l)
            return 1 + max(r, l)
        
        height(root)
        return diameter
