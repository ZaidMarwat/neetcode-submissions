class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1
        lowest = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                lowest = min(lowest, nums[l])
                return lowest
            
            m = (l+r)//2
            lowest = min(lowest, nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1

        return lowest