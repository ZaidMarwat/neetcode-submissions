"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        m = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            m[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = m[curr]
            copy.next = m[curr.next] if curr.next else None
            copy.random = m[curr.random] if curr.random else None
            curr = curr.next
        
        return m[head] if head else None