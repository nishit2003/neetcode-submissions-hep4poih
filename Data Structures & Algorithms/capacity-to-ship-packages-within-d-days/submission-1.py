class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        res = r

        def canship(cap):
            ship, curr = 1, cap
            for w in weights:
                if w > curr:
                    ship+=1
                    curr = cap
                curr-=w
            return ship <= days

        while l <= r:
            m = (l+r)//2
            if canship(m):
                res = m
                r = m - 1
            else:
                l = m +1
        return res