class TimeMap:
    def __init__(self):
        self.data = {}
        # self.time = 0

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([timestamp,value])
        # self.time-=1

    def get(self, key: str, timestamp: int) -> str:
        values = self.data.get(key,[])
        l,r = 0, len(values) - 1
        res = ""
        while l <= r:
            m = (l+r)//2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l=m+1
            else:
                r=m-1
        return res
