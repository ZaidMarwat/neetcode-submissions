class Solution:
    def longestPalindrome(self, s: str) -> str:
        idxl = idxr = 0
        largest = 0
        for i in range(len(s)):
            l,r = i,i
            count = 1
            while l >= 0 and r < len(s) and s[l]==s[r]:
                count += 2
                l -= 1
                r += 1

            if count > largest:
                largest = count
                idxl = l+1
                idxr = r-1

            l,r = i, i + 1
            count = 2
            while l >= 0 and r < len(s) and s[l]==s[r]:
                count += 2
                l -= 1
                r += 1
                
            if count > largest:
                largest = count
                idxl = l+1
                idxr = r-1
        
        return s[idxl:idxr+1]
