class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = {}
        topK = [[] for i in range(len(nums) + 1)]

        for n in nums:
            mp[n] = mp.get(n, 0) + 1

        for key, value in mp.items():
            topK[value].append(key)
        
        ret = []
        for i in range(len(topK) - 1, 0, -1):
            while topK[i]:
                ret.append(topK[i].pop())
                if len(ret) == k:
                    return ret
