from collections import defaultdict
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 1

        island_count = 0
        rows, cols = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c):
            if not(0 <= r < rows and 0 <= c < cols) or grid[r][c] != '1':
                return    
            grid[r][c] = '0'

            for dr, dc in DIRS:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c)
        
        return island_count