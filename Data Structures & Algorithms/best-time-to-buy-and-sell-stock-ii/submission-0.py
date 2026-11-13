class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prev = float('inf')
        res = 0
        for pr in prices:
            if pr > prev:
                res += pr-prev
            
            prev = pr

        return res