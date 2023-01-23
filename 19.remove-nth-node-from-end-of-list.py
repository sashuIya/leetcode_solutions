# Problem statement:
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# Solution illustration:
# https://github.com/sashuIya/leetcode_solutions/blob/master/images/19.remove-nth-node-from-end-of-list.png


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p0 = head
        p1 = head

        for i in range(n): 
            p1 = p1.next

        if p1 is None:
            return head.next 
        
        while p1.next != None:
            p0 = p0.next
            p1 = p1.next
        
        p0.next = p0.next.next

        return head