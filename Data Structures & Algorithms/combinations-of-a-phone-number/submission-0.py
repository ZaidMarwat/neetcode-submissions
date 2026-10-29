class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        n = len(digits)
        m = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        seen = [False]*n
        
        res = []
        def dfs(i, s):
            if len(s) == n:
                if s: 
                    res.append(s)
                return
            
            for ch in m[int(digits[i])]:
                dfs(i+1,s+ch)

        dfs(0, "")
        return res
