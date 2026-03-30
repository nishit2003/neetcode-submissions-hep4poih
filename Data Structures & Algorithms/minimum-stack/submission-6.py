class MinStack:
    def __init__(self):
        self.arr = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.minstack:
            self.minstack.append(min(val,self.minstack[-1]))
        else:
            self.minstack.append(val)
    def pop(self) -> None:
        if self.arr:
            self.arr.pop()
        if self.minstack:
            self.minstack.pop()
    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
