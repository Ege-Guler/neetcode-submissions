class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digits_to_letters = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        res, path = [], ""
        def dfs(start):
            nonlocal path

            if start == len(digits):
                if path == "":
                    return
                res.append(path[:])
                return

            for i in range(0, len(digits_to_letters[digits[start]])):
                
                path += digits_to_letters[digits[start]][i]
                dfs(start + 1)
                path = path[:len(path) -1]
        
        dfs(0)

        return res