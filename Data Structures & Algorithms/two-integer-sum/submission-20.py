class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = {}
        for i,val in enumerate(nums):
            diff = target - val
            if diff in numset:
                return [numset[diff],i]
            numset[val] = i
    