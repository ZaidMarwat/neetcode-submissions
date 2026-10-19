class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tm = {}
        for ch in t:
            tm[ch] = 1 + tm.get(ch,0)
        
        res = [-1,-1]
        minlen = float('inf')
        window = {}
        have, need = 0, len(tm)
        l = 0    
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch,0)

            if ch in tm and window[ch] == tm[ch]:
                have += 1
            
            while have == need:
                if r-l+1 < minlen:
                    res = [l,r]
                    minlen = r-l+1
                window[s[l]] -= 1
                if s[l] in tm and window[s[l]] < tm[s[l]]:
                    have -= 1
                l += 1
            
        l,r = res 
        return s[l:r+1] if res else ""
            
