class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dfs(rem):
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]

            best = float("inf")
            for c in coins:
                if c <= rem:
                    best = min(best, dfs(rem - c) + 1)
            memo[rem] = best
            return best
        
        res = dfs(amount)
        return -1 if res == float("inf") else res