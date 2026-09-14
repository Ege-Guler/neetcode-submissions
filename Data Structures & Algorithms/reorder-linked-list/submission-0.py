# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        middle = self.find_middle(head)
        second_half = middle.next   
        middle.next = None

        l1, l2 = head, self.reverse_list(second_half)

        temp = ListNode()
        current = temp

        c = 0
        while l1 and l2:
            if c % 2:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next
            c+=1
        current.next = l1 if l1 else l2

        head = current.next

    def find_middle(self, head: Optional[ListNode]) -> None:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverse_list(self, head: Optional[ListNode]) -> None:

        current = head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev



