class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row
        seen = set()
        for row in board:
            for val in row:
                if val == ".":
                    continue
                if val not in seen:
                    seen.add(val)
                else: return False
            seen.clear()
        #column
        for i, row in enumerate(board):
            for j in range(len(row)):
                val = board[j][i]
                if val == ".":
                    continue
                val = int(val)
                if val not in seen:
                    seen.add(val)
                else: return False
            seen.clear()
        #square
        for i in range(9):
            for j in range(9):
                row = (i // 3) * 3 + (j // 3)
                col = (i % 3) * 3 + (j % 3)
                val = board[row][col]
                if val == ".":
                    continue
                if val not in seen:
                    seen.add(val)
                else: return False
            seen.clear()

        return True