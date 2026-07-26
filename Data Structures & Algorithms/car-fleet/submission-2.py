class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        times = []

        x_v_pair = list(zip(position, speed))
        x_v_pair_sorted = sorted(x_v_pair, reverse=True)

        position, speed = zip(*x_v_pair_sorted)

        for i, pos in enumerate(position):
            dt = (target - pos) / speed[i]   
            times.append(dt)

        stack = []

        for i, t in enumerate(times):
            if i == 0:
                stack.append(t)
                continue
            if stack and stack[-1] < t:
                stack.append(t)


        return len(stack)
