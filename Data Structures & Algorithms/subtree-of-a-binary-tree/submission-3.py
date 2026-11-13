# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        
        if root is None:
            return False

        if subRoot is None:
            return False

        def find(root):
            if root is None:
                return False
            if isSame(root, subRoot):
                return True
            
            right = find(root.right)
            if right:
                return True
            return find(root.left)

        def isSame(root, subRoot):
            if root is None and subRoot is None:
                return True
            
            if root is None or subRoot is None:
                return False

            if root.val != subRoot.val:
                return False

            return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right) 

        
        return find(root)





