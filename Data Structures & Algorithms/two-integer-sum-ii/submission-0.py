class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        one = 0
        two = 0

        for i in range(len(numbers)):
            one = numbers[i]
            for j in range(len(numbers) - i - 1):
                two = numbers[i + j + 1]
                if one + two == target:
                    return [i + 1, i + j + 2]
                    
        return []