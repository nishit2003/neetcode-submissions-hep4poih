class MyCalendar:
    def __init__(self):
        self.stack = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s,e in self.stack:
            if e > startTime and s < endTime:
                return False
        self.stack.append([startTime,endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)