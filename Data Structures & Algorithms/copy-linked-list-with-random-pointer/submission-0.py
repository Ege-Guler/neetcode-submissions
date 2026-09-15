"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        cache = {} # id -> node

        current = head
        while current:
            cache[current] = Node(current.val)
            current = current.next
        
        current = head
        
        while current:
            cache[current].next = cache.get(current.next) #None by default
            cache[current].random = cache.get(current.random)
            current = current.next
        
        return cache[head]
