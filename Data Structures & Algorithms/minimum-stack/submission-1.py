class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.prefix_stack:
            new_min = min(self.prefix_stack[-1], val)
        else:
            new_min = val
        self.prefix_stack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.prefix_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix_stack[-1]
