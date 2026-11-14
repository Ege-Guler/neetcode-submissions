class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res, path = [], []

        def dfs(ix):

            if len(path) <= len(nums):
                if path not in res:
                    res.append(path[:])

            for i in range(ix, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return res