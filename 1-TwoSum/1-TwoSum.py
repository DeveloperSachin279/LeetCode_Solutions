# Last updated: 7/9/2026, 11:55:11 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
9        # Dummy node to act as the starting point of our result list
10        dummy = ListNode(0)
11        current = dummy
12        carry = 0
13        
14        # Continue looping as long as there are nodes in l1, l2, or a carry left over
15        while l1 or l2 or carry:
16            # Extract values if the nodes exist, otherwise use 0
17            val1 = l1.val if l1 else 0
18            val2 = l2.val if l2 else 0
19            
20            # Calculate the total sum for the current digit placement
21            total = val1 + val2 + carry
22            
23            # The new carry is the tens digit of the total
24            carry = total // 10
25            
26            # The new node's value is the ones digit of the total
27            current.next = ListNode(total % 10)
28            
29            # Move our pointers forward
30            current = current.next
31            if l1: l1 = l1.next
32            if l2: l2 = l2.next
33                
34        return dummy.next   