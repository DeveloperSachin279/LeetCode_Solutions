# Last updated: 7/9/2026, 11:56:09 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to act as the starting point of our result list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Continue looping as long as there are nodes in l1, l2, or a carry left over
        while l1 or l2 or carry:
            # Extract values if the nodes exist, otherwise use 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum for the current digit placement
            total = val1 + val2 + carry
            
            # The new carry is the tens digit of the total
            carry = total // 10
            
            # The new node's value is the ones digit of the total
            current.next = ListNode(total % 10)
            
            # Move our pointers forward
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return dummy.next   