class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l,r = 0, len(heights) - 1
        maxa = 0

        while l < r:
            maxa = max(maxa, (r - l) * min(heights[l],heights[r]))
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            
        return maxa
            

            