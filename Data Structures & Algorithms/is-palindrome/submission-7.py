class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.upper()
        new_s = ""

        for ch in s:
            if ch.isalnum():
                new_s += ch
        
        print(new_s)
        
        length = len(new_s)

        for i in range(length // 2):
            left = new_s[i]
            right = new_s[length - 1 - i]
            print(left)
            print(right)
            if left != right:
                return False
            
        
        return True