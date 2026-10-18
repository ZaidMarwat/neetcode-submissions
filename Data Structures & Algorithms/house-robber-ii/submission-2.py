class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def help(arr):
            rob1, rob2 = 0,0

            for num in arr:
                tmp = max(num+rob1, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2

        return max(help(nums[1:]), help(nums[:-1]))


