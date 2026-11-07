from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if len(grid) == 0:
            return 0

        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        while(q) and fresh > 0:
            # level
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if not(0 <= nc < cols and 0 <= nr < rows) or grid[nr][nc] != 1:
                        continue
                    fresh -= 1
                    grid[nr][nc] = 2
                    q.append((nr,nc))
            count += 1
            
    
        return count if fresh == 0 else -1


        
