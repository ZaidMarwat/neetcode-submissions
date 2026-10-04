class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        
        num = str(x) if not neg else str(x)[1:]
        num = num[::-1]
        if int(num) > (1<<31):
            return 0
        return int(num) if not neg else int(num) *-1
        
        