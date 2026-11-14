class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rows, cols = len(board), len(board[0])

        def dfs(r, c, k):

            if k == len(word):
                return True

            if not (0 <= r < rows and 0 <= c < cols) or word[k] != board[r][c]:
                return False

            temp = board[r][c]
            board[r][c] = '*'
            found = False
            for dr, dc in DIRS:
                found = dfs(dr + r, dc + c, k + 1) or found
            board[r][c] = temp

            return found

        truthy = False

        for row in range(rows):
            for col in range(cols):
                truthy = truthy or dfs(row, col, 0)

        return truthy