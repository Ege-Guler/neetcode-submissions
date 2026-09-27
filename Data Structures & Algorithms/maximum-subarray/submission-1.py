class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = max_sum = nums[0]

        l_ix = r_ix=start = 0

        for i in range(1, len(nums)):
            
            if nums[i] > cur + nums[i]:
                cur = nums[i]
                start = i
            else:
                cur += nums[i]

            if cur > max_sum:
                l_ix, r_ix = start, i
                max_sum = sum(nums[l_ix:r_ix + 1])
        
        return max_sum