class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for x1,y1 in points:
            for x2,y2 in points:
                if x1==x2 and y1==y2:
                    continue
                dist = abs(x1-x2) + abs(y1-y2)
                adj[(x1,y1)].append((dist,x2,y2))

        ret = 0
        seen = set()
        minHeap = [(0, points[0][0], points[0][1])]
        while minHeap:
            dist1,x1,y1 = heapq.heappop(minHeap)
            if (x1,y1) in seen:
                continue
            seen.add((x1,y1))
            ret += dist1
            for dist2,x2,y2 in adj[(x1,y1)]:
                if (x2,y2) in seen:
                    continue
                heapq.heappush(minHeap, (dist2,x2,y2))
        return ret


        