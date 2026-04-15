class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.plist = []

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1
        self.plist.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        x1,y1 = point
        for x2,y2 in self.plist:
            if abs(x2 - x1) == abs(y2-y1) and (x1 != x2 and y1 != y2):
                res += self.points[x1,y2] * self.points[x2,y1]
        return res