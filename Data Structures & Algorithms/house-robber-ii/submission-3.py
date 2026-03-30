class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            curr,prev = 0,0
            for num in nums:
                prev,curr = curr, max(curr,prev+num)
            return curr
        return max(nums[0],helper(nums[1:]),helper(nums[:-1]))