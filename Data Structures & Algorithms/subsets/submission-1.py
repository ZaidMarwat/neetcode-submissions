class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]

        # start with [[], [1]]  [] + [2], [1] + [2]

        for num in nums:
            res += [subset + [num] for subset in res]

        return res
