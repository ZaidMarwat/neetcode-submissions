class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        res = 0
        m = defaultdict(int)
        total = 0
        for i, num in enumerate(arr):
            total ^= num
            m[i] = total
        
        res = [m[j]^m[i-1] for i,j in queries]
        return res























        # m = defaultdict(int)
        # res = []
        # total = 0
        # for i, num in enumerate(arr):
        #     total ^= num
        #     m[i] += total
        
        # for i,j in queries:
        #     res.append(m[i-1]^m[j])
        
        # return res
