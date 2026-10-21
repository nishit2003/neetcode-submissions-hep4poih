class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        curr = 0
        l = 0
        res = len(nums)
        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target:
                res = min(res,r-l+1)
                curr -= nums[l]
                l+=1
        return res

# nums = [2,3,1,2,4,3]
# target = 7
# curr = 2
# l = 0
# res = inf
# len(nums) = 5
