class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        
        def pali(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        def dfs(i, comb):
            if i >= len(s):
                res.append(comb.copy())
                return
            
            for j in range(i,len(s)):
                if pali(i,j):
                    comb.append(s[i:j+1])
                    dfs(j+1,comb)
                    comb.pop()
        
        dfs(0,[])
        return res
