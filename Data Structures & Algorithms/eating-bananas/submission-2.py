from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hours(k: int): #k eating speed
            return sum([ceil(banana / k) for banana in piles])

        lo, hi = 1, max(piles)
        while lo < hi:
            k = (lo + hi) // 2

            if hours(k) <= h:
                hi = k
            else:
                lo = k + 1
        return lo
