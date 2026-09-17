class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)

        for n in nums:
            m[n] += 1
        
        arr = []
        for n, c in m.items():
            arr.append([c,n])
        arr.sort()

        ret = []
        while len(ret) < k:
            ret.append(arr.pop()[1])
        
        return ret

