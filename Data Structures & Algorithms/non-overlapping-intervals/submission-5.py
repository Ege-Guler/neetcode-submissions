class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))

        pivot = intervals[0]
        res = []
        
        def overlap(x, y):
            return x[0] < y[1] and y[0] < x[1] 

        for ix, interval in enumerate(intervals):
            if ix == 0:
                continue
            
            if overlap(interval, pivot):
                if interval[1] < pivot[1]:
                    pivot = interval
                continue
            res.append(pivot)
            pivot = interval 
        res.append(pivot)
        return len(intervals) - len(res)
            