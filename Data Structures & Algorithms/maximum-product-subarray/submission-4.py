class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # brute force
        # res = float('-inf')
        # s = len(nums)
        
        # for i in range(s):
        #     product = 1
        #     for j in range(i,s):
        #         product *= nums[j]
        #         res = max(res, product)

        # return res

        max_res = min_res = res = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_res, min_res = min_res, max_res

            max_res = max(num, max_res * num)
            min_res = min(num, min_res * num)

            res = max(res, max_res)

        return res