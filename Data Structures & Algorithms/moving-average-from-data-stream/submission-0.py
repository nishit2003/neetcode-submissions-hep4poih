class MovingAverage:

    def __init__(self, size: int):
        self.windowSum=0
        self.window=collections.deque()
        self.size=size

    def next(self, val: int) -> float:
        self.windowSum+=val
        self.window.append(val)
        if len(self.window)>self.size:
            self.windowSum-=self.window.popleft()
        return self.windowSum/len(self.window)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
