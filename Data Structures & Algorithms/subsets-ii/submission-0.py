class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        res = []

        # 1,1,2
        def dfs(i, sub):
            if i >= n:
                res.append(sub.copy())
                return
            
            sub.append(nums[i])
            dfs(i+1, sub)
            sub.pop()
            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, sub)
        
        dfs(0, [])
        return res
