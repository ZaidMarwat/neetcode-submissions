class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        chars = defaultdict(int)
        res = 0
        maxf = 0
        for r in range(len(s)):
            chars[s[r]] += 1
            maxf = max(maxf, chars[s[r]])

            if r-l+1 - maxf > k:
                chars[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res