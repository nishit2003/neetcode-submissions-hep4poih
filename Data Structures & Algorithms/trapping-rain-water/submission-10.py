class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = [0] * len(height)
        maxr = [0] * len(height)

        maxl[0] = height[0]
        for i in range(1,len(height)):
            maxl[i] = max(maxl[i-1],height[i])
        
        maxr[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            maxr[i] = max(maxr[i+1],height[i])

        res = 0
        for i in range(len(height)):
            res += min(maxl[i],maxr[i]) - height[i]

        return res