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

        m = defaultdict(lambda: Node(0))
        m[None] = None

        curr = head
        while curr:
            m[curr].val = curr.val
            m[curr].next = m[curr.next]
            m[curr].random = m[curr.random]
            curr = curr.next
        
        return m[head]