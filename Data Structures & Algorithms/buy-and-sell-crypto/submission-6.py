class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest = prices[0]
        maxp = 0
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            else:
                maxp = max(maxp, prices[i] - lowest)
            
        return maxp
