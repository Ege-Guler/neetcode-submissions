class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                ans[j] *= nums[i]
        return ans