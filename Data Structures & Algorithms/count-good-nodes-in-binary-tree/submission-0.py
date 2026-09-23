# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0

        def preOrder(root, max_val):
            nonlocal count

            if not root:
                return

            if root.val >= max_val:
                count += 1
            max_val = max(max_val, root.val)

            preOrder(root.left, max_val)
            preOrder(root.right, max_val)
        
        preOrder(root, root.val)
        return count