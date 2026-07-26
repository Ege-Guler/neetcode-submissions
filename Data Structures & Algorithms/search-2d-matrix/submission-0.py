class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        flattened_matrix = []
        for row in matrix:
            if row[self.binary_search(0, len(row) - 1, target, row)] == target:
                return True
        return False


    def binary_search(self, l: int, r: int, target: int, nums: List[int]) -> int:

        m = (r - l) // 2 + l

        if nums[m] == target:
            return m

        if(l < r):

            if target < nums[m]:
                return self.binary_search(l, m - 1, target, nums)
            else:
                return self.binary_search(m + 1, r, target, nums)

        return -1