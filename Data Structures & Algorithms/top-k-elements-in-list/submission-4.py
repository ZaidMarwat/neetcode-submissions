class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        m = defaultdict(int)

        for i in range(len(nums)):
            m[nums[i]] += 1

        arr = []
        for num, count in m.items():
            arr.append([count,num])
        arr.sort()

        ret = []
        while len(ret) < k:
            ret.append(arr.pop()[1])
        return ret
            