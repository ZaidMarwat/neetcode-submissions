class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        l = len(nums)

        for i in range(l):
            if nums[i] in s:
                return True
            
            s.add(nums[i])

        return False
