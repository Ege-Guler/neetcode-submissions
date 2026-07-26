class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        l = 0
        r = m * n - 1

        return self.binary_search(l, r, target, matrix) != -1
        

    def binary_search(self, l: int, r: int, target: int, matrix: List[List[int]]) -> int:

        m = (r - l) // 2 + l

        row, col = m // len(matrix[0]), m % len(matrix[0]) 

        if matrix[row][col] == target:
            return m

        if(l < r):

            if target < matrix[row][col]:
                return self.binary_search(l, m - 1, target, matrix)
            else:
                return self.binary_search(m + 1, r, target, matrix)

        return -1