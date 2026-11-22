class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        dp = [False] * (target + 1)

        dp[0] = True

        for x in nums:
            for sum_ in range(target, x - 1, -1):
                if dp[sum_ - x] == True:
                    dp[sum_] = True
        
        return dp[-1]