class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good_ix = len(nums) - 1

        for i in range(len(nums) -2 , -1, -1):
            if nums[i] + i >= good_ix:
                good_ix = i
        return good_ix == 0