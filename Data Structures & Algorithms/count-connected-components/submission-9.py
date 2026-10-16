class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        res = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            res += 1
            q = deque([i])
            visited.add(i)
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
        
        return res

