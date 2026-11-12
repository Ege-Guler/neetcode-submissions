class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax = rmax = 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                lmax = max(height[l], lmax)
                water += lmax - height[l]
                l += 1
            else:
                rmax = max(height[r], rmax)
                water += rmax -  height[r]
                r -= 1
        return water