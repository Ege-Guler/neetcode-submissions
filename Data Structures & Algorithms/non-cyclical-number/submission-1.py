class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        num = n

        def is_non_cyclical(n):
            temp = 0
            for s in str(n):
                temp += int(s) ** 2
            
            return temp

        while num not in seen:
            seen.add(num)
            num = is_non_cyclical(num)
            if num == 1:
                return True
        
        return False


              