from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []
        
        level = 0
        queue = deque([(root, level)])
        while queue:
            node, level = queue.popleft()
            res.append([node.val, level])

            if node.left is not None:
                queue.append([node.left, level + 1])
            if node.right is not None:            
                queue.append([node.right, level + 1])
        
        levels = defaultdict(list)
        for val, lvl in res:
            levels[lvl].append(val)

        return list(levels.values())