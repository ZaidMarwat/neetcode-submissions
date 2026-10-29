class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        h = []
        for n in nums:
            if len(h) == k:
                heapq.heappushpop(h, n)
            else:
                heapq.heappush(h, n)
        
        return h[0]

