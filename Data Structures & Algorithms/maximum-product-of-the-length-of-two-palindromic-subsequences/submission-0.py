class Solution:
    def maxProduct(self, s: str) -> int:

        ret = 0
        def dfs(i,s1,s2):
            nonlocal ret
            if i > len(s)-1:
                if isPali(s1) and isPali(s2):
                    ret = max(ret, len(s1)*len(s2)) 
                return
            dfs(i+1, s1+s[i], s2)
            dfs(i+1, s1, s2+s[i])
            dfs(i+1, s1, s2)
            return 
            
        def isPali(word):
            return word == word[::-1]
        
        dfs(0,"","")
        return ret

