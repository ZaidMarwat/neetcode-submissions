# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        end = count - n

        curr = head
        prev = None
        while end:
            end -= 1
            prev = curr
            curr = curr.next
        
        if curr == head:
            return curr.next
        else:
            prev.next = curr.next
            return head


            