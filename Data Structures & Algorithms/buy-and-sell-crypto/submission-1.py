class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0

        if len(prices) < 2:
            return 0

        lmin = prices[0]
        lmax = prices[1]

        for i in range(len(prices)):
            if prices[i] < lmin:
                lmin = prices[i]
                lmax = 0
            
            if prices[i] > lmax:
                lmax = prices[i]

            if lmin < lmax:
                ret = max(ret, lmax - lmin)
            
        
        return ret
