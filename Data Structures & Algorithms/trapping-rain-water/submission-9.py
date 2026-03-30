class Solution:
    def trap(self, height: List[int]) -> int:
        # res = 0
        # maxL = [0] * len(height)
        # maxR = [0] * len(height)

        # maxL[0] = height[0]
        # for i in range(1, len(height)):
        #     maxL[i] = max(height[i],maxL[i-1])
        
        # maxR[-1] = height[-1]
        # for i in range(len(height)-2,-1,-1):
        #     maxR[i] = max(height[i],maxR[i+1])

        
        # for i in range(len(height)):
        #     res += min(maxL[i],maxR[i]) - height[i]

        # return res
        res = 0
        l,r = 0, len(height) - 1
        maxl, maxr = height[l],height[r]

        while l<r:
            if height[l] < height[r]:
                l+=1
                maxl = max(maxl, height[l])
                res += maxl - height[l]

            else:
                r-=1
                maxr = max(maxr,height[r])
                res += maxr - height[r]

        return res
