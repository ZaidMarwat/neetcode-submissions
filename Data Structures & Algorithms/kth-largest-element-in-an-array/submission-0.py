class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify_max(nums)
        for _ in range(k):
            ret = heapq.heappop_max(nums)
        return ret

