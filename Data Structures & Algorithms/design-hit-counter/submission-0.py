class HitCounter:

    def __init__(self):
        self.hits=[] #stores timestamp

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # binary search
        l,r=0,len(self.hits)
        while l<r:
            mid=(r-l)//2+l
            if self.hits[mid]<=timestamp:
                l=mid+1
            else:
                r=mid
        right=l

        l,r=0,len(self.hits)
        while l<r:
            mid=(r-l)//2+l
            if self.hits[mid]<=timestamp-300:
                l=mid+1
            else:
                r=mid
        
        return right-l


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
