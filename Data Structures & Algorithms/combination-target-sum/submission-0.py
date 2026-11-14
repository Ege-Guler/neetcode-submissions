class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path = [], []

        def dfs(index):

            if sum(path) == target:
                res.append(path[:])
            if sum(path) > target:
                return

            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i)
                path.pop()

        dfs(0)
        return res
