class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = ""
        for c in s:
            if c.isalnum():
                n += c.lower()
        return n == n[::-1]

