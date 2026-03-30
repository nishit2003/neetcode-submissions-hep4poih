class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0
        l , r = 0 , len(height)-1
        MaxL = height[l]
        MaxR = height[r]

        while l < r:
            if MaxL < MaxR:
                l += 1
                MaxL = max(height[l], MaxL)
                res += MaxL - height[l]
                

            else:
                r-=1
                MaxR = max(height[r], MaxR)
                res += MaxR - height[r]


        return res