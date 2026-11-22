class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}

        def dfs(start):
            if len(s) == start:
                return True
            if start in memo:
                return memo[start]

            for end in range(start + 1, len(s) + 1):
                if s[start: end] in wordDict:
                    if dfs(end):
                        memo[start] = True
                        return True
            memo[start] = False
            return False
        
        return dfs(0)