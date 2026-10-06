class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])
        count = 0
        prevEnd = float('-inf')

        for start, end in intervals:
            if start >= prevEnd:
                count += 1
                prevEnd = end
        
        return len(intervals) - count
