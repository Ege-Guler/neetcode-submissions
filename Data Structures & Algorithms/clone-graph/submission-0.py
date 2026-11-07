"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque, defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None:
            return None

        q = deque([node])

        old_new = defaultdict(list)
        old_new[node] = Node(node.val)

    
        while q:
            curr = q.popleft()

            for v in curr.neighbors:
                if v not in old_new:
                    old_new[v] = Node(v.val)
                    q.append(v)
                old_new[curr].neighbors.append(old_new[v])
                    
        
        return old_new[node]


