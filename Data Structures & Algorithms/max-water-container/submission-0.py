class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i, j = 0, len(heights) - 1


        a = 0

        while i < j:

            h = min(heights[i], heights[j])
            b = j - i

            temp_area = b * h

            if temp_area > a:
                a = temp_area

            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return a