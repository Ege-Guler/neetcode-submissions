class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures)

        for ix, temperature in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temperature  :
                prev_ix = stack.pop()
                res[prev_ix] = ix - prev_ix

            stack.append(ix)

        
        return res