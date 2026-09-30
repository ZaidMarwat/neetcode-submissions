# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        while n:
            n -= 1
            curr = curr.next
        
        if not curr:
            return head.next
        
        first, second = head, curr
        while second.next:
            first = first.next
            second = second.next
        
        first.next = first.next.next
        
        return head

