class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:

            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid

            #[1,2,3,4,5,6] #right is sorted
            if nums[mid] < nums[hi]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

            #[3,4,5,6,1,2] #left is sorted
            else: # nums[mid] > nums[hi]
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

        return -1