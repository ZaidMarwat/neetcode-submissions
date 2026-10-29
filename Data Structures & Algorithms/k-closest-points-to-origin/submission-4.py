class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        h = []

        for x,y in points:
            heapq.heappush_max(h, [x*x + y*y, x, y])
            if len(h) > k:
                heapq.heappop_max(h)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1:])
        return res
            
