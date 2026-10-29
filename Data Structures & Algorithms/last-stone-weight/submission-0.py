class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            left = abs(first-second)
            if left > 0:
                heapq.heappush_max(stones, left)
        
        return stones[0] if stones else left