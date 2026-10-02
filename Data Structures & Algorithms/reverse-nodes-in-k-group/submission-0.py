class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        curr = head
        count = head

        ret = head
        for _ in range(k - 1):
            ret = ret.next
            if not ret:
                return head

        prev_tail = None

        while count:
            for _ in range(k - 1):
                count = count.next if count else None
                if not count:
                    count = -1
                    break

            if count == -1:
                break

            new_head, new_tail, curr = self.reverseK(curr, k)

            if prev_tail:
                prev_tail.next = new_head

            prev_tail = new_tail
            count = curr

        return ret

    def reverseK(self, head, k):
        curr = head
        prev = None

        for i in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        head.next = curr
        return prev, head, curr