"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            time.append([i.start, 1])
            time.append([i.end, -1])
        
        time.sort()

        res = 0
        rn = 0
        for _, room in time:
            rn += room
            res = max(res, rn)
        
        return res
            
