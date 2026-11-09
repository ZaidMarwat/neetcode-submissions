class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)
        for fr,to,price in flights:
            adj[fr].append((to,price))
        
        minHeap = [(0,0,src)]
        cheapest = {(src, 0): 0}

        while minHeap:
            price,step,node = heapq.heappop(minHeap)
            if node == dst:
                return price
            if step-1 == k:
                continue
            if (node,step) in cheapest and cheapest[(node,step)] < price:
                continue
            cheapest[(node,step)] = price
            
            for nei, pr in adj[node]:
                heapq.heappush(minHeap,(price+pr,step+1,nei))
        
        return -1