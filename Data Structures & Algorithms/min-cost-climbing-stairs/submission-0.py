class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] + [float('inf')] * len(cost)
        dp[0] = 0
        dp[1] = 0
        
        for stair in range(2, len(cost) + 1):
            dp[stair] = min(dp[stair - 1] + cost[stair - 1], dp[stair -2] + cost[stair -2])
        
        return dp[len(cost)]