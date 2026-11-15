class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res, path = [], []

        def isPalindrome(s):
            return s == s[::-1]

        def dfs(index):
            
            if index == len(s):
                res.append(path[:])
                return
            
            for end in range(index, len(s)):

                if not isPalindrome(s[index:end + 1]):
                    continue

                path.append(s[index:end + 1])
                dfs(end + 1)
                path.pop()
        
        dfs(0)
        return res