class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key= lambda x: x[0])
        end = intervals[0][1]
        remove_cnt = 0

        for s, e in intervals[1:]:
            if end > s:
                remove_cnt += 1
                end = min(e, end)
            else:
                end = e
        
        return remove_cnt
