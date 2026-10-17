class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = [[] for i in range(n+1)]

        for a,b,t in times:
            adj[a].append((b,t))
        
        shortest = [float('inf')] * (n+1)
        shortest[k] = 0
        shortest[0] = 0
        seen = set()
        q = deque([k])
        seen.add(k)
        elapsed = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei, time in adj[node]:
                    if time + shortest[node] < shortest[nei]:
                        shortest[nei] = time + shortest[node]
                        q.append(nei)
                        

        return max(shortest) if max(shortest) != float('inf') else -1
            
            




