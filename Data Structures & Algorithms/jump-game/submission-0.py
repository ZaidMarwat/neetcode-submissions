class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        reach = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= reach:
                goal = i
                reach = 1
            else:
                reach += 1
            
        return goal == 0

            

            