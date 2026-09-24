class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        length = len(height)
        leftarr = [0] * length
        rightarr = [0] * length

        leftmax = 0
        for i in range(length):
            leftmax = max(height[i], leftmax)
            leftarr[i] = leftmax

        rightmax = height[length - 1]
        rightarr[i] = rightmax
        for i in range(length - 2, -1, -1):
            rightmax = max(height[i], rightmax)
            rightarr[i] = rightmax
            
        
        for i in range(length):
            res += min(leftarr[i], rightarr[i]) - height[i]

        return res
            

            