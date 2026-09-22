class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        ret = 0

        nums.sort()

        streak = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - prev == 1:
                streak += 1
            elif nums[i] - prev == 0:
                continue
            else:
                ret = max(ret, streak)
                streak = 1
            
            prev = nums[i]
        
        if streak > ret:
            ret = streak

        return ret
