"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) == 0:
            return True
        def overlap(x, y):
            return x.start < y.end and y.start < x.end

        intervals.sort(key=lambda x: (x.start, x.end))
        pivot = intervals[0]
        for ix, interval in enumerate(intervals):
            if ix == 0:
                continue
            if overlap(pivot, interval):
                return False
            pivot = interval
        
        return True