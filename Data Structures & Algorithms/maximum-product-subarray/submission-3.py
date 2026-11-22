class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        best =  min_ = max_ = nums[0]
        for i in range(1, len(nums)):

            x = nums[i]

            temp = (x, x * min_, x * max_)

            min_, max_ = min(temp), max(temp)
            best = max(best, max_)
        return best