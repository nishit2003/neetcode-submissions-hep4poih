class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0 ,len(nums) - 1
        res = float('inf')
        while l<=r:
            m = (l+r)//2
            if nums[m] >= nums[r]: # smallest val is in right side
                l = m + 1
            else: #min val is in left side
                r= m -1
            res = min(res,nums[m])
        return res
