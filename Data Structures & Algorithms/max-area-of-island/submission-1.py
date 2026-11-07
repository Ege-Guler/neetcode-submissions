class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if len(grid) == 0:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if not(0 <= r < rows and 0<= c < cols) or grid[r][c] != 1:
                return 0
            area = 1
            grid[r][c] = 0
            for dr, dc in DIRS:
                area += dfs(r + dr, c + dc)

            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                area = 0
                if grid[r][c] == 1:
                    max_area = max(dfs(r, c), max_area)
        
        return max_area