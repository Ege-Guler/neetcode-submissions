class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        if len(nums) <= 2:
            return max(nums)

        def _robHouse(nums:List[int]) -> int:

 


            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for h in range(2, len(nums)):
                dp[h] = max(dp[h -1], dp[h - 2] + nums[h])        
            
            return dp[-1]
        
        return max(_robHouse(nums[:len(nums) - 1]), _robHouse(nums[1:]))