class Solution:
    def maxProduct(self, s: str) -> int:
        N = len(s)
        pali = {}
        for mask in range(1, 1<<N):
            s1 = ""
            for i in range(N):
                if mask & (1<<i):
                    s1 += s[i]
            if s1 == s1[::-1]:
                pali[mask] = len(s1)
        
        ret = 0
        for s1 in pali:
            for s2 in pali:
                if not s1&s2:
                    ret = max(ret,pali[s1]*pali[s2])
        return ret

