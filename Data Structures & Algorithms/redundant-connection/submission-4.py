class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj = [[] for i in range(len(edges)+1)]

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

            seen = set()
            q = deque()
            q.append((a, -1))
            while q:
                node, parent = q.popleft()
                for nei in adj[node]:
                    if parent == nei:
                        continue
                    if nei in seen:
                        return [a,b]
                    seen.add(nei)
                    q.append((nei,node))
                

