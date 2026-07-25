class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = ["+", "-", "*", "/"]
        
        for token in tokens:
            if token in ops:
                
                r = int(stack.pop())
                l = int(stack.pop())
                res = None
                if token == "+":
                    res = l + r
                     
                elif token == "-":
                    res = l - r
                elif token == "*":
                    res = l * r
                else:
                    res = int(l / r)
                
                stack.append(res)
                continue
            stack.append(token)

        return int(stack.pop())