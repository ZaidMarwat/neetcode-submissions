class Solution:
    def combinationSum2(self, candidates, target):

        candidates.sort()
        n = len(candidates)
        res = []
        s = set()

        def dfs(i, comb, t):
            if t == target:
                l = comb.copy()
                if tuple(l) not in s:
                    res.append(comb.copy())
                    s.add(tuple(l))
                return
            if i >= n or t > target:
                return

            comb.append(candidates[i])
            dfs(i+1, comb, t+candidates[i])
            comb.pop()
            while i < n-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, comb, t)
        
        dfs(0,[],0)
        return res
