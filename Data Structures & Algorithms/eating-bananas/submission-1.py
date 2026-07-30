from math import ceil

class Solution:


    def calcHours(self, piles, h, k):
        return sum(ceil(pile / k) for pile in piles ) 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2
            hours = self.calcHours(piles, h, mid)

            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left
