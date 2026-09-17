class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')

        left = right = 0
        cursum = 0

        for i in range(len(nums)):
            if cursum < 0:
                cursum = 0
            cursum += nums[i]
            maximum = max(cursum, maximum)
        
        return maximum