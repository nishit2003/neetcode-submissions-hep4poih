class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        def helper(arr):
            res = arr[0]
            curr = 0

            for ele in arr:
                if curr < 0:
                    curr = 0
                
                curr += ele
                res = max(res,curr)
            return res

        # case 1 - middle array
        normal = helper(nums)
        # return normal

        # case 2 - all negs
        if normal < 0:
            return normal
        
        # case 3 - circular
        neg_array = [-x for x in nums]
        min_array = -helper(neg_array)
        circular = sum(nums) - min_array

        return max(normal,circular)