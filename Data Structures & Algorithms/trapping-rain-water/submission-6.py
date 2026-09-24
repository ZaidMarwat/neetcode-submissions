class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1

        leftmax = height[l]
        rightmax = height[r]

        ret = 0
        while l < r:
            if leftmax < rightmax:
                ret += leftmax - height[l]
                l += 1
                leftmax = max(leftmax, height[l])

            else:
                ret += rightmax - height[r]
                r -= 1
                rightmax = max(rightmax, height[r])
        
        return ret
