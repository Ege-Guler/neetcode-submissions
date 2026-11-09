from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sources):
            seen = set(sources)
            q = deque(sources)

            while q:
                r, c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if not(0 <= nr <  rows and 0 <= nc < cols) or (nr, nc) in seen:
                        continue

                    if heights[nr][nc] >= heights[r][c]: 
                        seen.add((nr, nc))
                        q.append((nr, nc))
            return seen

        
        pacific = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        two_way = bfs(pacific) & bfs(atlantic)

        return [list(cell) for cell in two_way]
