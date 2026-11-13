class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        leftpass = ""
        depth = 0
        for ch in s:
            if ch == '(':
                depth += 1
            elif ch == ')':
                if depth == 0:
                    continue
                depth -= 1
            leftpass += ch
        
        print(leftpass)
        rightpass = ""
        depth = 0
        for ch in reversed(leftpass):
            if ch == ')':
                depth += 1
            elif ch == '(':
                if depth == 0:
                    continue
                depth -= 1
            rightpass += ch
        
        return rightpass[::-1]
