class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        s = len(nums)
        
        for i in range(s):
            product = 1
            for j in range(i,s):
                product *= nums[j]
                res = max(res, product)

        return res