class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0

        jump = 0
        while(r < len(nums) - 1):
            max_jump = 0
            for i in range(r, l-1, -1):
                max_jump =  max(nums[i] + i, max_jump)  #max jump 
            l = r + 1
            r = max_jump
            jump += 1
        return jump