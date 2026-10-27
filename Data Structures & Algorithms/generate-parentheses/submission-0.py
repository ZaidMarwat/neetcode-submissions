class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        l = n*2
        res = []

        def dfs(d, s):
            if len(s) == l and d == 0:
                res.append(s)
                return
            if d > n or d < 0 or len(s) > l:
                return
            
            s += "("
            dfs(d+1, s)
            s = s[:-1]
            s += ")"
            dfs(d-1, s)

        dfs(0,"")

        return res