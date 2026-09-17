from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        


        return self.inOrder(p, q)

    def inOrder(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            if p == None and q == None:
                return True

            if p != None and q == None or p == None and q != None:
                return False
            if p.val != q.val:
                return False

            i = self.inOrder(p.left, q.left)
            j = self.inOrder(p.right, q.right)
            return i and j