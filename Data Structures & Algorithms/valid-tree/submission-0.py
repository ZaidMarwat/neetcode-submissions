class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        seen = set()
        q = deque()
        q.append((0,-1))
        seen.add(0)
        while q:
            print(q)
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in seen:
                    return False
                seen.add(nei)
                q.append((nei,node))
        print(len(seen), n)
        return len(seen) == n

