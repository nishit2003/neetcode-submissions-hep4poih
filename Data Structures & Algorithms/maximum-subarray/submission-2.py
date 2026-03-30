class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # space - o(n^2) time - o(1)
        # n = len(nums)
        # res = nums[0]
        # for i in range(n):
        #     curr = 0
        #     for j in range(i,n):
        #         curr += nums[j]
        #         res = max(res, curr)

        # return res

        curr = 0
        res = nums[0]

        for num in nums:
            if curr < 0:
                curr = 0
            curr+=num
            res = max(res,curr)

        return res

