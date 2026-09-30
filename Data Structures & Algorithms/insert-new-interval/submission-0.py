class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        start, end = newInterval

        i = 0
        while i < n and intervals[i][1] < start:
            i += 1

        j = i
        while j < n and intervals[j][0] <= end:
            start = min(start, intervals[j][0])
            end = max(end, intervals[j][1])
            j += 1

        intervals[i:j] = [[start, end]]
        return intervals