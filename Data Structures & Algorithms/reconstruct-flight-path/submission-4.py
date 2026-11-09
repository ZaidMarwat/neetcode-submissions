class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(deque)
        for fr, to in sorted(tickets):
            adj[fr].append(to)

        res = []
        def dfs(node): 
            while adj[node]:
                dfs(adj[node].popleft())
            res.append(node)
        
        dfs('JFK')
        return res[::-1]