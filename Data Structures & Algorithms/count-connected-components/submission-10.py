class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for i in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        print(adj)
        
        res = 0
        seen = set()
        for i in range(n):
            if i in seen:
                continue
            res += 1

            q = deque()
            q.append(i)
            seen.add(i)
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
            
            print(seen)
        
        return res


