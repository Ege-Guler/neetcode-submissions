class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2
        memo = {}

        def dfs(i, rem):
            if rem == 0:
                return True
            if i == len(nums) or rem < 0:
                return False
            if (i, rem) in memo:
                return memo[(i, rem)]

            memo[(i, rem)] = dfs(i + 1, rem - nums[i]) or dfs(i + 1, rem)
            return memo[(i, rem)]

        return dfs(0, target) 