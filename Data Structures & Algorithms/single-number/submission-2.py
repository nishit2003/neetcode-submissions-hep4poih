class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = nums[0]

        for i in nums[1:]:
            tmp = tmp ^ i
        return tmp