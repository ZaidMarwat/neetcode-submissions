class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        counts = defaultdict(int)
        for ch in s1:
            counts[ch] += 1
        
        wincounts = defaultdict(int)
        for ch in s2[:len(s1) - 1]:
            wincounts[ch] += 1

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            wincounts[s2[r]] += 1
            
            if counts == wincounts:
                return True

            wincounts[s2[l]] -= 1

            if wincounts[s2[l]] == 0:
                del wincounts[s2[l]]

            l += 1
            r += 1
    
        return False