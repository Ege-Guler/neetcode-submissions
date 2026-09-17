# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if root is None:
            return None

        if q.val < p.val:
            p, q = q, p 

        l_val, r_val = p.val, q.val

        val = root.val
        if l_val <= val and r_val >= val:
            return root
        elif val > r_val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif val < l_val:
            return self.lowestCommonAncestor(root.right, p, q)
