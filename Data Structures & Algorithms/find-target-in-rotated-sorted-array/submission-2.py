class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)
        
    def binary_search(self, nums: List[int], target: int, low: int, high: int) -> int:
        while low <= high:

            mid = (low + high) // 2

            if target == nums[mid]:
                return mid
            
            if nums[low] <= nums[mid]:

                if nums[low] <= target < nums[mid]:
                    high = mid -1
                else: # target < nums[low]
                    low = mid + 1

            else:

                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1