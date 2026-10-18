class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            subs = [dp[k] for k in range(i) if nums[k]<nums[i]]
            dp[i] = 1 + max(subs) if subs else 1
        
        return max(dp)