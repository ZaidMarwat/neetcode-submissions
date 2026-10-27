class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        seen = [False] * n
        res = []
        def dfs(i, c, perm):
            if c == n:
                res.append(perm.copy())
                return 
            
            for i in range(n):
                if not seen[i]:
                    perm.append(nums[i])
                    seen[i] = True
                    dfs(i+1,c+1,perm)
                    perm.pop()
                    seen[i] = False
        

        dfs(0,0,[])
        return res