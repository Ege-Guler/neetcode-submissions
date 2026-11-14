class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], []

        def dfs(open_, close):

            if len(path) == 2 * n:
                
                res.append(''.join(path))
                return

            if open_ < n:
                path.append("(")
                dfs(open_ + 1, close)
                path.pop()
            
            if close < open_:
                path.append(")")
                dfs(open_, close + 1)
                path.pop()

        dfs(0, 0)
        return res