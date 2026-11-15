class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        res = [intervals[0]]

        for interval in intervals[1:]:
            if res[-1][1] >= interval[0]:
                if res[-1][1] >= interval[1]:
                    continue
                res[-1][1] = interval[1]
            
            else:
                res.append(interval)
        
        return res