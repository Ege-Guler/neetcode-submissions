class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxDp = [0] * n
        minDp = [0] * n
        minDp[0] = maxDp[0] = nums[0]

        for i in range(1, n):
            x = nums[i]
            temp = (x, x * minDp[i-1], x * maxDp[i-1])
            minDp[i], maxDp[i] = min(temp), max(temp)

        return max(maxDp) 
