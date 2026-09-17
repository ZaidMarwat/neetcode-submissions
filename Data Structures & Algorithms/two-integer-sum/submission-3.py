class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        m = {}

        for i in range(len(nums)):
            r = target - nums[i]

            if r in m:
                return [m[r], i]
            
            m[nums[i]] = i