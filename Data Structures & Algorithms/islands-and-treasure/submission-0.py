from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        DIRS=[(1,0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        level = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if not(0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != 2147483647:
                        continue
                    
                    grid[nr][nc] = level
                    q.append((nr, nc))
            level += 1
