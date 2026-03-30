class Solution:
    def trap(self, h: List[int]) -> int:
        res = 0
        l,r = 0 , len(h) - 1
        maxL, maxR = h[l], h[r]

        while l<r:
            if h[l] < h[r]:
                l+=1
                maxL = max(maxL, h[l])
                res += maxL - h[l]
            else:
                r-=1
                maxR = max(maxR, h[r])
                res += maxR - h[r]
        return res