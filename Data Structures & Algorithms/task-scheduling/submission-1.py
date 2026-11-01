class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        m = defaultdict(int)
        for t in tasks:
            m[t] += 1
        
        maxF = max(m.values())
        numMaxF = sum(1 for v in m.values() if v==maxF)
        return max(len(tasks), (maxF-1)*(n+1) + numMaxF)