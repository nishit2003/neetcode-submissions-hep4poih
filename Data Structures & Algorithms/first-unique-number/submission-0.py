class FirstUnique:

    def __init__(self, nums: List[int]):
        # counter map, queue
        self.numCounter={}
        self.queue=collections.deque()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:
        if value not in self.numCounter:
            self.numCounter[value]=0
        self.numCounter[value]+=1
        self.queue.append(value)
        while self.queue and self.numCounter[self.queue[0]]>1:
            self.queue.popleft()


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
