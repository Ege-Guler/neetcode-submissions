from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])
        DIRS = [(1, 0) , (-1, 0), (0, 1), (0, -1)]

        border_sources = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)]
        
        q = deque((r, c) for r, c in border_sources if board[r][c] == 'O')
        seen = set(q)

        while q:
            r, c = q.popleft()

            for dr, dc in DIRS:
                nr, nc = dr + r, dc + c

                if (0 <= nr < rows) and (0 <= nc < cols) and board[nr][nc] == 'O' and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc))
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and board[row][col] == 'O':
                    board[row][col] = 'X'
            


