class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(comb, i, t):
            if t == target:
                res.append(comb.copy())
            if i >= len(nums) or t > target:
                return
            
            comb.append(nums[i])
            dfs(comb, i, t+nums[i])
            comb.pop()
            dfs(comb, i+1, t)

        dfs([],0,0)
        ret = [list(x) for x in {tuple(t) for t in res}]
        
        return ret
