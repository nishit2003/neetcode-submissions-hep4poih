class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxL = [0] * len(height)
        maxR = [0] * len(height)

        maxL[0] = height[0]
        for i in range(1, len(height)):
            maxL[i] = max(height[i],maxL[i-1])
        
        maxR[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            maxR[i] = max(height[i],maxR[i+1])

        
        for i in range(len(height)):
            res += min(maxL[i],maxR[i]) - height[i]

        return res