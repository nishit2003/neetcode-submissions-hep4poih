class MedianFinder:

    def __init__(self):
        self.val = []
        
    def addNum(self, num: int) -> None:
        self.val.append(num)
        self.val.sort()

    def findMedian(self) -> float:
        size = len(self.val)
        if  size % 2 != 0:
            return self.val[size//2]
        else:
            mid = size/2
            return (self.val[size // 2 -1] + self.val[size//2])/2

        