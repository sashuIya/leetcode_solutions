# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None

        prev = None
        current = head
        current_next = head.next

        new_head = head

        while current and current_next:
            if prev:
                prev.next = current_next
            else:
                new_head = current_next
            current.next, current_next.next = current_next.next, current

            prev = current
            current = current.next
            if current:
                current_next = current.next

        return new_head
