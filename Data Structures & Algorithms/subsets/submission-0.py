class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def dfs(index):
            if index == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[index])
            dfs(index + 1)
            path.pop()
            dfs(index + 1)
        
        dfs(0)
        return res