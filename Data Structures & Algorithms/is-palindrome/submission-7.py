class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == None: return True
        s = ''.join(c.lower() for c in s if c.isascii() and c.isalnum())

        start, end = 0, len(s) - 1

        if len(s) == 0: return True

        while s[start] == s[end]:
            start += 1
            end -=1
            if start >= end:
                return True

        return False
            

        
        