# o(n) solution

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if nums is []:
            return 0

        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for h in range(2, len(nums)):
            dp[h] = max(dp[h - 2] + nums[h],
                        dp[h - 1])

        return dp[-1]