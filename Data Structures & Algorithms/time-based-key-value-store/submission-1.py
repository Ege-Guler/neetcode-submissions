from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.store[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]  # [[], [], []]
        if arr ==[]: return ""

        greater_than_timestamp = bisect.bisect_right(arr, timestamp, key=lambda x:x[0])

        if arr[:greater_than_timestamp] == []:
            return ""
        
        return arr[greater_than_timestamp - 1][1]
