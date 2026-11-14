class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], []

        def isValid(paranthesis):

            s = ''.join(paranthesis)
            stack = []
            
            for ch in s:
                if ch == ")":
                    if not stack or stack[-1] != "(":
                        return False
                    stack.pop()
                else:
                    stack.append(ch)

            return not stack

        def dfs():

            if len(path) == 2 * n:
                if isValid(path):
                    res.append(''.join(path[:]))
            if len(path) > 2*n:
                return

            for i in ["(", ")"]:
                path.append(i)
                dfs()
                path.pop()

        dfs()
        return res