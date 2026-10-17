class Solution:
    def climbStairs(self, n: int) -> int:
        
        first = 1
        second = 1

        res = 1
        for i in range(2, n + 1):
            res = first + second
            first = second
            second = res
        
        return res
