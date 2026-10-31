class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.MinStack:
            self.MinStack.append(min(self.MinStack[-1], val))
        else:
            self.MinStack.append(val)
    def pop(self) -> None:
        if self.stack and self.MinStack:
            self.stack.pop(-1)
            self.MinStack.pop(-1)
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
        
