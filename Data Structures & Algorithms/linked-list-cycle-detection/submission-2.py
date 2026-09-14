# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        current = head

        while current:
            if id(current) in seen:
                return True
            seen.add(id(current))
            current = current.next
        return False