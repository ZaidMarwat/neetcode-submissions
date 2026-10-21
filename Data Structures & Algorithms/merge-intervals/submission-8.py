class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = []
        prevEnd = float('-inf')

        for start, end in intervals:
            if prevEnd >= start:
                if end > prevEnd:
                    res[-1][1] = end
            else:
                res.append([start,end])

            prevEnd = res[-1][1]

        
        return res