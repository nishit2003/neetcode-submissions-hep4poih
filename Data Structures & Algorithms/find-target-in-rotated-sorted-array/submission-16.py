class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # print(nums.index(target))
        if target in nums:
            return nums.index(target)
        else:
            return -1