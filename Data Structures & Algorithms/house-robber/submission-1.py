class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            money = nums[i]    
            for j in range(i - 1):
                dp[i] =  max(dp[i], dp[j] + money)
        
        return max(dp)