class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        r = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            r[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            r[i] *= postfix
            postfix *= nums[i]
        
        return r
