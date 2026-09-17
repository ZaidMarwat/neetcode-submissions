class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroes = 0

        for n in nums:
            if n == 0:
                zeroes += 1
                if zeroes > 1:
                    return [0] * len(nums)
            else:
                product *= n
        
        res = [0] * len(nums)
        for i, n in enumerate(nums):
            if zeroes:
                res[i] = 0 if n else product
            else:
                res[i] = product // n
        return res