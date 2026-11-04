class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = [[] for _ in range(n+1)]
        for ui,vi,ti in times:
            adj[ui].append((vi,ti))

        q = deque()
        q.append((k,0))
        seen = defaultdict(lambda: float('inf'))
        seen[k] = 0

        while q:
            node, time = q.popleft()
            for target, weight in adj[node]:
                if time+weight < seen[target]:
                    seen[target] = time+weight
                    q.append((target, seen[target]))
        
        return max(seen.values()) if len(seen) == n else -1