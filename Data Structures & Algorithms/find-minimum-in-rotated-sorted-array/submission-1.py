class Solution:
    def findMin(self, nums: List[int]) -> int:
        #  0 1 2 3 4 5
        # [3,4,5,6,1,2]
        #

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1
                
            else: 
                hi = mid
        
        return nums[lo]