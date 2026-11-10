class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if matrix is None:
            return False

        rows, cols = len(matrix), len(matrix[0])

        lo, hi = 0, (rows*cols) - 1


        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid//cols][mid%cols] == target:
                return True
            elif target < matrix[mid//cols][mid%cols]:
                hi = mid - 1
            else:
                lo = mid + 1
        

        return False

    
