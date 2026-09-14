# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1, num2 = self.list_to_num(l1), self.list_to_num(l2)

        total = num1 + num2

        total = [int(digit) for digit in str(total)]
        
        total_list = ListNode()
        current = total_list

        for digit in reversed(total):
            current.next = ListNode(digit)
            current = current.next

        return total_list.next    
    
    def list_to_num(self, head: Optional[ListNode]) -> int:

        current = head

        num = 0
        exponent = 0
        ten = 10
        while current:
            num += current.val * (ten ** exponent)
            exponent += 1
            current = current.next
        
        return num