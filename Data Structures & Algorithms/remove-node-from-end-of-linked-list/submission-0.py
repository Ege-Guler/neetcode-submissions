# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        list_len = self.list_length(head)

        if list_len == 0 or n > list_len: return head

        if list_len -n == 0:
            next_node = head.next
            head.next = None
            head = next_node
            return head

        counter = 0
        current = head
        while current:
            counter+=1
            if counter == list_len - n:
                current.next = current.next.next
                continue
            current = current.next

        return head


    def list_length(self, head: Optional[ListNode]) -> int:
        
        if head == None: return 0
        i = 0
        current = head
        while current:
            i+=1
            current = current.next
        
        return i
    
