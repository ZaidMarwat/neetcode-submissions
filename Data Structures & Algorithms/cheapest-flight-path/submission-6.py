class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)
        for fr, to, price in flights:
            adj[fr].append((to, price))

        seen = set()
        minHeap = [(0, 0, src)]

        while minHeap:
            cost, numStops, node = heapq.heappop(minHeap)

            if (node, numStops) in seen:
                continue

            seen.add((node, numStops))

            if node == dst:
                return cost

            for to, price in adj[node]:
                if numStops + 1 <= k + 1:
                    heapq.heappush(minHeap, (cost + price, numStops + 1, to))

        return -1