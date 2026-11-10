class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        m = defaultdict(int)
        m[0] += 1
        res = 0
        total = 0
        for num in nums:
            total += num
            res += m[total-goal]
            m[total] += 1
        return res

