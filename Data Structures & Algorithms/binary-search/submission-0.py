class Solution:
    def search(self, nums: List[int], target: int) -> int:

        return self.binary_search(target, 0, len(nums) - 1, nums)
    
    def binary_search(self, target: int,l:int , r:int , nums: List[int]) -> int:


        m = (l + r) // 2

        if nums[m] == target:
            return m
        
        if(l < r):

            if target < nums[m]:
                return self.binary_search(target, l, m - 1, nums)    
            else:
                return self.binary_search(target, m + 1, r, nums)
        return -1