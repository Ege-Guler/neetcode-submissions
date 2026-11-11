from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.kv_store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.kv_store[key]

        return self.binary_search(0, len(arr) - 1, timestamp, arr)

    def binary_search(self, lo:int, hi:int, target:int, nums: list):
        res = ""
        while lo <= hi:

            mid = (lo + hi) // 2

            if nums[mid][1] <= target:
                res = nums[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res