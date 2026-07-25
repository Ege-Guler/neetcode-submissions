class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for paran in s:

            if paran in ["(", "{", "["]:
                stack.append(paran)

            else:
                if len(stack) == 0: return False
                temp = stack.pop()

                if paran == ")":
                    if temp != "(": return False 
                elif paran == "}":
                    if temp != "{": return False 
                else:
                    if temp != "[": return False 

        return len(stack) == 0