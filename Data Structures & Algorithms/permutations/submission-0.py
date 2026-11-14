class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def dfs():
            if len(path) == len(nums):
                res.append(path[:])

            for i in range(0, len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs()
                path.pop()
        
        dfs()
        return res